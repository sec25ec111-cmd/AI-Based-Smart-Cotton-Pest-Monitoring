from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo11n.pt")

# Run pest detection on an image
results = model("data/test.jpg")

# Display results
for result in results:
    result.show()
    