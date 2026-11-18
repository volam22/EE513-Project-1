"""MTF50 estimator used for both real RAW images and the synthetic-edge test."""

import cv2
import numpy as np
from scipy.signal import savgol_filter


def measure_mtf50(image_roi):
    image_roi = image_roi.astype(np.float64)
    H, W = image_roi.shape

    # Detect edge using a local gradient centroid
    smooth = cv2.GaussianBlur(
        image_roi.astype(np.float32), (5, 5), 1.0
    )
    grad = cv2.Sobel(
        smooth, cv2.CV_32F, 1, 0, ksize=3
    )

    coarse = np.argmax(np.abs(grad), axis=1)
    edge_x = []

    for row in range(H):
        c = int(coarse[row])
        lo = max(0, c - 5)
        hi = min(W, c + 6)

        weights = np.abs(grad[row, lo:hi])
        positions = np.arange(lo, hi)

        if weights.sum() == 0:
            raise ValueError("No detectable edge in a row")

        edge_x.append(
            np.sum(positions * weights) / weights.sum()
        )

    m, b = np.polyfit(np.arange(H), edge_x, 1)
    angle = np.degrees(np.arctan(abs(m)))

    # Project samples onto the edge normal
    yy, xx = np.indices((H, W))
    distance = (xx - m * yy - b) / np.sqrt(1 + m**2)

    # Supersampled ESF
    bin_width = 0.25
    bins = np.arange(-12, 12 + bin_width, bin_width)

    sums, _ = np.histogram(
        distance.ravel(),
        bins=bins,
        weights=image_roi.ravel()
    )
    counts, _ = np.histogram(distance.ravel(), bins=bins)

    if np.any(counts == 0):
        raise ValueError("Empty ESF bins")

    esf = sums / counts

    # ESF -> LSF -> normalized MTF
    esf_smooth = savgol_filter(esf, 9, 3)
    lsf = np.gradient(esf_smooth, bin_width)

    lsf_windowed = lsf * np.hanning(len(lsf))

    mtf = np.abs(np.fft.rfft(lsf_windowed))
    mtf /= mtf[0]

    freq = np.fft.rfftfreq(len(lsf_windowed), d=bin_width)

    crossings = np.where(mtf <= 0.5)[0]
    if len(crossings) == 0 or crossings[0] == 0:
        raise ValueError("No valid MTF50 crossing")

    i = crossings[0]

    mtf50 = np.interp(
        0.5,
        [mtf[i], mtf[i-1]],
        [freq[i], freq[i-1]]
    )

    return mtf50, angle
