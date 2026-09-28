# Pherosense AI-SDG: SENSE.DETECT.GREEN

AI-powered smart cotton pest monitoring system combining computer vision, IoT concepts, and Qualcomm AI Hub optimization for Snapdragon-powered devices.

## Overview

Pherosense AI-SDG is a smart agriculture solution designed to support early detection of cotton pests using an AI-based computer vision model.

The system is designed to capture pest images, identify pest categories, estimate pest occurrence, and provide actionable monitoring information for farmers.

For the Snapdragon AI Lab Build & Present Challenge, the trained YOLO11n model was exported to ONNX and compiled and profiled using Qualcomm AI Hub for a Snapdragon X Elite CRD.

## Problem Statement

Cotton crops can be affected by pests such as bollworms, whiteflies, thrips, and other harmful insects. Manual monitoring can be time-consuming and may delay detection.

Pherosense aims to provide an AI-assisted approach for faster pest identification and monitoring.

## Proposed Solution

The system combines:

- AI-based pest detection
- Image-based computer vision
- ESP32 / ESP32-CAM based sensing concept
- Soil monitoring sensors
- Pest monitoring and counting
- Pheromone trap integration concept
- Farmer notification concept
- Snapdragon-optimized AI inference

## AI Model

### YOLO11n Pest Detection

The pest detection model was trained using a cotton pest dataset containing:

- 2,038 images
- 7 pest classes
- YOLO-format annotations
- CC BY 4.0 licensed dataset

### Pest Classes

1. American Bollworm
2. Aphid Colony
3. Jassid Leafhopper
4. Mealybug
5. Pink Bollworm
6. Thrips
7. Whitefly Adult

## Model Validation Results

The trained YOLO11n model achieved the following validation results:

| Metric | Result |
|---|---:|
| Precision | 81.7% |
| Recall | 64.1% |
| mAP@50 | 66.0% |
| mAP@50-95 | 47.5% |

These results were obtained on the validation dataset used during model development.

## Qualcomm AI Hub Optimization

The trained YOLO11n model was exported to ONNX format and prepared for Qualcomm AI Hub compilation.

### Snapdragon Target

**Device:** Snapdragon X Elite CRD  
**Operating System:** Windows 11  
**Runtime:** ONNX

The model was successfully compiled using Qualcomm AI Hub.

### AI Hub Results

- Compile Job ID: `jg9z7n2vp`
- Compiled Model ID: `mq33g2xrq`
- Profile Job ID: `j5wl0eqmp`

### Snapdragon X Elite Profile

| Metric | Result |
|---|---:|
| Minimum Inference Time | 5.7 ms |
| Median Inference Time | 5.8 ms |
| Estimated Peak Memory | 5 MB |
| NPU Compute Units | 334 |

The reported performance values are from Qualcomm AI Hub profiling on the Snapdragon X Elite CRD.

> Note: The developer's local computer used during model development is an Intel-based PC. The Snapdragon performance values above were obtained through Qualcomm AI Hub cloud profiling and should not be interpreted as measurements from a locally owned Snapdragon laptop.

## System Workflow

```text
Image Capture
      ↓
YOLO11n AI Pest Detection
      ↓
Pest Classification
      ↓
Pest Count / Monitoring
      ↓
Threshold-Based Decision
      ↓
Farmer Notification
      ↓
Pheromone Trap / Control Concept

## Proposed Hardware Components

- ESP32
- ESP32-CAM
- Soil Moisture Sensor
- Soil pH Sensor
- Temperature Sensor
- UV LED / Light Trap
- Pheromone Trap
- Servo Motor
- Battery / Solar Power Supply
- Connecting Wires
## Software and Technologies

- Python
- Ultralytics YOLO11n
- ONNX
- Qualcomm AI Hub
- OpenCV
- Arduino IDE
- ESP32 / ESP32-CAM
- Flutter / Mobile Application
AI-Based-Smart-Cotton-Pest-Monitoring/
│
├── data/
│   └── Cotton-pests-Detection.v6i.yolov11/
│
├── docs/
│
├── models/
│
├── results/
│
├── src/
│   └── detect_pest.py
│
├── runs/
│   └── detect/
│
├── README.md
└── requirements.txt
## Sustainability

Pherosense AI-SDG promotes sustainable cotton cultivation through AI-assisted pest monitoring.

The system is designed to:

- Support early identification of cotton pests
- Enable data-driven pest monitoring
- Support targeted pest management
- Help reduce unnecessary pesticide application
- Reduce manual monitoring effort
- Promote environmentally responsible agricultural practices
## SDG Alignment

### Primary SDG – SDG 15: Life on Land

The project supports sustainable land and agricultural ecosystem management through AI-based pest monitoring and responsible pest-management practices.

### Additional SDG Relevance

- **SDG 2 – Zero Hunger:** Supports healthier crop production through early pest monitoring.
- **SDG 9 – Industry, Innovation and Infrastructure:** Applies AI, IoT, and edge-AI technologies to agriculture.
- **SDG 12 – Responsible Consumption and Production:** Supports more targeted use of agricultural inputs.
- **SDG 13 – Climate Action:** Promotes technology-assisted and resource-conscious farming practices.
## Future Scope

- Multi-crop pest detection
- Offline mobile AI inference
- Solar-powered field deployment
- Weather-based pest risk prediction
- Satellite-based crop stress monitoring
- Automated pest-control mechanisms
- Expanded Qualcomm AI Hub optimization
- Edge AI deployment on Snapdragon-powered devices
- Cloud-based farmer monitoring dashboard
- Real-time pest population tracking
## Dataset Attribution

The cotton pest detection model was trained using the Cotton Pests Detection Dataset, Version 6, from Roboflow Universe.

- Dataset Source: Roboflow Universe
- Project: Cotton Pests Detection
- Version: 6
- License: CC BY 4.0

Source:
https://universe.roboflow.com/shoaib-btznm/cotton-pests-detection/dataset/6

The dataset attribution and license requirements should be retained when using or redistributing the dataset.
## Institution

**Department of Electronics and Communication Engineering**  
**Sri Sairam Engineering College**

## Project

**Pherosense AI-SDG: SENSE.DETECT.GREEN**

Developed as an academic and research project and adapted for the Snapdragon AI Lab Build & Present Challenge.