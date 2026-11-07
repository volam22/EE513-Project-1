
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

The third radial distortion coefficient (k3) was fixed at zero. The calibration was also evaluated using an independent straight-edge test.

### 3.2 Spatial Resolution (MTF)

Used a slanted-edge target to estimate MTF50 at the image center and four off-center regions. Five RAW images were analyzed at each location using the green Bayer channel.

### 3.3 Sensor Noise

Used 10 pairs of RAW flat-field images at ISO 64 to estimate conversion gain and read noise using the Poisson–Gaussian model and difference-of-pairs method.

Read noise was also measured independently using five short-exposure dark frames.

### 3.4 Dynamic Range

Calculated dynamic range using the observed green-channel RAW saturation signal and one RMS temporal read-noise level as the lower threshold.

### 3.5 Color Accuracy

Used three ColorChecker charts to fit 3 × 3 color correction matrices and evaluate CIEDE2000 color errors before and after correction.

The analysis used the ColorChecker24 – After November 2014 reference dataset. An additional experiment evaluated one fixed LED-fitted CCM under different lighting conditions.

## 4. Results

| Measurement | Result | Uncertainty | Units |
|---|---:|---:|---|
| Focal length (fx) | 2786.07 | 11.03 | pixels |
| Focal length (fy) | 2791.50 | 10.45 | pixels |
| Estimated focal length | 6.798 | 0.027 | mm |
| Principal point (cx) | 1501.06 | 5.76 | pixels |
| Principal point (cy) | 2003.55 | 7.76 | pixels |
| Radial distortion (k1) | 0.0552 | 0.0030 | Dimensionless |
| Radial distortion (k2) | -0.0493 | 0.0037 | Dimensionless |
| Tangential distortion (p1) | -0.0001 | 0.0006 | Dimensionless |
| Tangential distortion (p2) | -0.0017 | 0.0007 | Dimensionless |
| RMS reprojection error | 0.8946 | Not estimated | pixels |
| Center MTF50 | 0.3730 | 0.0063 | cycles/green-plane pixel |
| Mean off-center MTF50 | 0.3391 | 0.0013 | cycles/green-plane pixel |
| Conversion gain | 0.24371 | 0.00191 | DN/e⁻ |
| Read noise | 6.5692 | 0.0552 | e⁻ RMS |
| Shot/read-noise crossover | 43.15 | 0.72 | e⁻ |
| Dark-current fitted slope | +0.6762 | 0.1332 | e⁻/s |
| Dynamic range | 10.8904 | 0.0043 | stops |
| Mean ΔE2000 before CCM | 13.514 | 0.620 | Dimensionless |
| Mean ΔE2000 after CCM | 3.472 | 0.215 | Dimensionless |
| Mean worst-patch ΔE2000 | 7.552 | 0.223 | Dimensionless |

**Notes:**
- The focal length in millimeters assumes an effective pixel pitch of 2.44 µm.
- MTF50 uncertainties describe measurement repeatability, not the total variation across the sensor.
- Dark current was not reliably resolved because the fitted slope changed sign when the longest exposure was excluded.
- The dynamic-range estimate is conditional on the observed saturation plateau. Its uncertainty does not include systematic saturation effects.
- The color accuracy results represent in-sample CCM performance.

## 5. Verification

- **Geometry:** The final calibration reduced straight-edge RMS deviation from 2.769 to 1.634 pixels, an improvement of approximately 41%.
- **MTF50:** A synthetic Gaussian-edge test measured 0.1877 cycles/pixel compared with a theoretical value of 0.1874 cycles/pixel (approximately 0.16% error).
- **Sensor Noise:** Single-frame variance produced a photon-transfer slope approximately 15% higher than the difference-of-pairs method.
- **Dynamic Range:** The observed saturation plateau was 3567 DN, compared with a DNG metadata white level of 4095 DN. The two interpretations produced estimates of 10.89 and 11.12 stops.
- **Color Accuracy:** A fixed LED-fitted CCM produced mean ΔE2000 values of 3.72 under LED lighting, 6.59 under incandescent lighting, and 8.73 under daylight.

## 6. Reproducibility and Tests

### 6.1 Running the Project

The camera characterization analysis was completed using Python and Jupyter Notebook.

1. Download or clone this repository.
2. Open `EE513_Project1_Camera_Characterization_Labeled.ipynb` in JupyterLab.
3. Install the Python packages required by the notebook.
4. Update the image folder paths to match the locations of the RAW DNG files.
5. Select **Kernel → Restart Kernel and Run All Cells**.

The notebook runs the five camera characterization analyses in sequence and displays the calculated measurements, figures, and verification results.

The final measurements and uncertainties are recorded in `results.json`.

### 6.2 Verification Tests

The notebook includes checks to evaluate the reliability of the calculations.

- **MTF50:** Tested the slanted-edge algorithm using a synthetic Gaussian-blurred edge with a known theoretical MTF50. The calculated result differed from theory by approximately 0.16%.
- **Sensor Noise:** Compared single-frame and paired-frame variance estimation methods to evaluate the effects of fixed spatial variations.
- **Final Results:** Checked that the main calculated measurement values were finite.

The complete notebook was executed successfully using the original RAW images.

### 6.3 Reproducibility Notes

The analysis requires the original RAW DNG images and the Python libraries imported by the notebook.

Some file paths are specific to my computer and must be updated before running the notebook on another system.

If the original DNG images are not included in this repository, the analysis cannot be fully reproduced without those input files.

The final report contains additional details about the methods, uncertainties, and limitations.

## 7. Project Deliverables

- `README.md` - Project overview, methods, results, and verification
- `results.json` - Final measurement values and uncertainties
- Jupyter notebook - Camera characterization analysis and calculations
- Final report - Datasheet, decisions-and-verification statement, and AI usage disclosure

## 8. Course Information

Portland State University

EE513 - Image Processing

Project 1: Characterize Your Camera

Professor James McNames
