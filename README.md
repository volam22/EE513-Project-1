# EE513 Project 1: Camera Characterization

## 1. Project Overview

This project characterizes the imaging performance of the main rear camera on an iPhone 14 Pro using RAW image measurements and Python-based analysis.

The objective is to measure camera performance beyond the manufacturer's specifications, including lens distortion, spatial resolution, sensor noise, dynamic range, and color accuracy.

## 2. Camera and Equipment

- **Camera:** iPhone 14 Pro, main rear camera (1×)
- **RAW Capture App:** RAW Camera
- **Programming Language:** Python
- **Software:** OpenCV, NumPy, Matplotlib, and other required libraries
- **Image Format:** DNG 

All measurements will use the same physical camera to maintain consistency.

## 3. Measurement Methods

### 3.1 Camera Calibration and Lens Distortion

Use checkerboard images and OpenCV camera calibration to estimate intrinsic camera parameters, lens distortion coefficients, and reprojection error.

### 3.2 Spatial Resolution (MTF)

Use a slanted-edge target to estimate the modulation transfer function (MTF), including MTF50 at the image center and four corners.

### 3.3 Sensor Noise

Use RAW flat-field images at different exposures to estimate conversion gain, read noise, and a Poisson-Gaussian noise model.

### 3.4 Dynamic Range

Calculate dynamic range using the saturation signal and measured noise floor.

### 3.5 Color Accuracy

Use ColorChecker images to fit a color correction matrix and evaluate color differences before and after correction.

## 4. Results

Results will be updated as measurements are completed. Each numerical result will include an uncertainty.

| Measurement | Result | Uncertainty | Units |
|---|---|---|---|
| Focal length | Pending | Pending | pixels |
| Lens distortion | Pending | Pending | — |
| RMS reprojection error | Pending | Pending | pixels |
| Center MTF50 | Pending | Pending | cycles/pixel |
| Corner MTF50 | Pending | Pending | cycles/pixel |
| Conversion gain | Pending | Pending | DN/electron |
| Read noise | Pending | Pending | electrons |
| Dynamic range | Pending | Pending | stops |
| Mean color difference | Pending | Pending | Delta E |


## 8. Course Information

Portland State University

EE513 - Image Processing

Project 1: Characterize Your Camera
