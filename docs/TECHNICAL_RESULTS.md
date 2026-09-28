# Pherosense AI-SDG – Technical Results

## AI Model

The project uses a YOLO11n object detection model for cotton pest detection.

### Dataset

- Dataset: Cotton Pests Detection
- Version: 6
- Images: 2,038
- Classes: 7
- License: CC BY 4.0

### Pest Classes

- American Bollworm
- Aphid Colony
- Jassid Leafhopper
- Mealybug
- Pink Bollworm
- Thrips
- Whitefly Adult

## Model Validation

The trained model was evaluated on the validation dataset.

| Metric | Result |
|---|---:|
| Precision | 81.7% |
| Recall | 64.1% |
| mAP@50 | 66.0% |
| mAP@50-95 | 47.5% |

## ONNX Conversion

The trained YOLO11n model was exported to ONNX format for deployment and Qualcomm AI Hub compilation.

- Model format: ONNX
- Input size: 640 × 640
- Model file size: approximately 10.1 MB
- Output shape: 1 × 11 × 8400

## Qualcomm AI Hub Compilation

The ONNX model was prepared for Qualcomm AI Hub and successfully compiled for:

**Target Device:** Snapdragon X Elite CRD  
**Operating System:** Windows 11  
**Runtime:** ONNX

### Compilation Evidence

- Compile Job ID: `jg9z7n2vp`
- Compiled Model ID: `mq33g2xrq`

## Snapdragon X Elite Profiling

The compiled model was successfully profiled on the Snapdragon X Elite CRD using Qualcomm AI Hub.

### Profiling Results

| Metric | Result |
|---|---:|
| Minimum Inference Time | 5.7 ms |
| Median Inference Time | 5.8 ms |
| Estimated Peak Memory | 5 MB |
| NPU Compute Units | 334 |

### Profile Evidence

- Profile Job ID: `j5wl0eqmp`

The reported inference-time measurements are from Qualcomm AI Hub profiling on the Snapdragon X Elite CRD.

## Development Environment

The model was developed and tested locally on an Intel-based Windows PC. Snapdragon performance measurements were obtained separately through Qualcomm AI Hub profiling.

## Summary

The project demonstrates an end-to-end AI deployment workflow:

```text
Cotton Pest Dataset
        ↓
YOLO11n Training
        ↓
Model Validation
        ↓
ONNX Export
        ↓
Qualcomm AI Hub Compilation
        ↓
Snapdragon X Elite Profiling
        ↓
Edge AI Deployment Readiness