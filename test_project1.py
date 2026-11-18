"""Known-answer checks for the functions used in the Project 1 notebook."""

import numpy as np
from scipy.ndimage import gaussian_filter

from camera_mtf import measure_mtf50
from camera_noise import paired_temporal_variance


def test_gaussian_edge_mtf50():
    # I used a Gaussian edge because its MTF50 is known from theory.
    height, width = 260, 120
    sigma = 1.0
    yy, xx = np.indices((height, width))
    edge = np.where(xx < 50 + np.tan(np.deg2rad(4.596)) * yy, 1070.0, 565.0)
    blurred = gaussian_filter(edge, sigma=sigma)

    measured, angle = measure_mtf50(blurred)
    expected = np.sqrt(np.log(2)) / (np.sqrt(2) * np.pi * sigma)
    error_pct = abs(100 * (measured - expected) / expected)
    assert error_pct < 1.0, f"MTF50 error: {error_pct:.3f}%"
    assert 3.0 < angle < 6.0


def test_paired_temporal_variance():
    # Both images share a fixed pattern that should cancel when subtracted.
    rng = np.random.default_rng(42)
    height, width = 512, 512
    sigma = 5.0
    pattern = 0.1 * np.arange(width)[None, :]
    a = 1000 + pattern + rng.normal(0, sigma, (height, width))
    b = 1000 + pattern + rng.normal(0, sigma, (height, width))

    measured = paired_temporal_variance(a, b)
    expected = sigma**2
    assert abs(measured - expected) / expected < 0.03
    assert paired_temporal_variance(a, a) == 0.0
