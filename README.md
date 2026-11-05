
# EE513 Project 1: Camera Characterization

## 1. Project Overview

This project characterizes the imaging performance of the main rear camera on an iPhone 14 Pro using RAW image measurements and Python-based analysis.

The objective is to measure camera performance beyond the manufacturer's specifications, including lens distortion, spatial resolution, sensor noise, dynamic range, and color accuracy.

## 2. Camera and Equipment

- **Camera:** iPhone 14 Pro, main rear camera (1×)
- **RAW Capture App:** RawCam
- **Programming Language:** Python
- **Software:** Jupyter Notebook, OpenCV, NumPy, Matplotlib
- **Image Format:** Bayer RAW (BGGR), DNG

All measurements used the same physical camera to maintain consistency.

## 3. Measurement Methods

### 3.1 Camera Calibration and Lens Distortion

Used 16 checkerboard images and OpenCV camera calibration to estimate intrinsic camera parameters, lens distortion coefficients, and reprojection error.

### 3.2 Spatial Resolution (MTF)

Used a slanted-edge target to estimate MTF50 at the image center and four off-center regions. Measurements were performed on the green Bayer RAW plane.

### 3.3 Sensor Noise

Used 10 pairs of RAW flat-field images at ISO 64 to estimate conversion gain and read noise using the Poisson–Gaussian model and difference-of-pairs method.

### 3.4 Dynamic Range

Calculated dynamic range using the observed RAW saturation signal and one RMS temporal read-noise level as the lower threshold.

### 3.5 Color Accuracy

Used three ColorChecker charts to fit 3 × 3 color correction matrices and evaluate CIEDE2000 color errors before and after correction.

## 4. Results

| Measurement | Result | Uncertainty | Units |
|---|---:|---:|---|
| Focal length (fx) | 2786.07 | 11.03 | pixels |
| Focal length (fy) | 2791.50 | 10.45 | pixels |
| RMS reprojection error | 0.8946 | Not estimated | pixels |
| Center MTF50 | 0.3730 | 0.0063 | cycles/green-plane pixel |
| Mean off-center MTF50 | 0.3391 | 0.0013 | cycles/green-plane pixel |
| Conversion gain | 0.24371 | 0.00191 | DN/e⁻ |
| Read noise | 6.5692 | 0.0552 | e⁻ RMS |
| Dark-current fitted slope | +0.6762 | 0.1332 | e⁻/s |
| Dynamic range | 10.8904 | 0.0043 | stops |
| Mean ΔE before CCM | 13.514 | 0.620 | ΔE2000 |
| Mean ΔE after CCM | 3.472 | 0.215 | ΔE2000 |
| Mean worst-patch ΔE | 7.552 | 0.223 | ΔE2000 |

**Notes:** Dark current was not reliably resolved. The dynamic-range value is conditional on the observed saturation plateau, and its uncertainty does not include systematic saturation effects. Color results represent in-sample CCM performance.

## 5. Verification

- **Geometry:** Straight-edge RMS improved from 2.769 to 1.634 pixels after undistortion.
- **MTF50:** Synthetic Gaussian-edge test measured 0.1877 cycles/pixel versus 0.1874 theoretically (approximately 0.16% error).
- **Noise:** Single-frame variance produced a photon-transfer slope approximately 15% higher than the paired-frame method.
- **Dynamic Range:** Observed and metadata-based calculations differed by approximately 0.23 stops.
- **Color Accuracy:** A fixed CCM produced mean ΔE2000 values of 3.72 (LED), 6.59 (incandescent), and 8.73 (daylight).

## 6. Reproducibility and Tests

The project analysis was performed using Python and Jupyter Notebook. Final measurements and uncertainties are recorded in `results.json`.

**One-command reproduction:** Not yet implemented or verified.

**Automated tests:** Test commands and coverage have not yet been verified.

The exact installation and execution commands will be documented after confirming the repository's files and dependencies.

## 7. Project Deliverables

- `README.md` — Project overview, methods, results, and verification
- `results.json` — Final measurement values and uncertainties
- Final report — Datasheet and decisions-and-verification statement

## 8. Course Information

Portland State University

EE513 — Image Processing

Project 1: Characterize Your Camera

Professor James McNames
