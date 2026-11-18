"""Paired-frame noise calculation used in the Project 1 notebook."""

import numpy as np


def paired_temporal_variance(frame_a, frame_b):
    """Estimate temporal variance from two RAW images at the same exposure."""
    a = np.asarray(frame_a, dtype=np.float64)
    b = np.asarray(frame_b, dtype=np.float64)
    if a.shape != b.shape or a.size < 2:
        raise ValueError("The two frames need matching shapes and at least two pixels")
    return float(np.var(a - b, ddof=1) / 2)
