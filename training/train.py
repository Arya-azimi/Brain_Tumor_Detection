from ultralytics import YOLO

model = YOLO("yolov8s-cls.pt")
model.train(
    data="../data",
    epochs=10,
    imgsz=224,
    batch=16,
    device="cpu",
)