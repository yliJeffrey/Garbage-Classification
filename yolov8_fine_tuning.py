from ultralytics import YOLO

# Build a YOLOv9c model from pretrained weight
model = YOLO("yolov8m-cls.pt")

# Display model information (optional)
model.info()

# Train the model on the dataset for 200 epochs
results = model.train(data="dataset", epochs=200, imgsz=400, batch=32, patience=20)
