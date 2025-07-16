# from ultralytics import YOLO

# model = YOLO("yolov8s.pt")

# model.train(
#     data="dataset/data.yaml", 
#     epochs=50,                 
#     imgsz=640,
#     batch=16,                  
#     device="cpu"
# )



# from ultralytics import YOLO

# model = YOLO('/content/best.pt')

# model.train(
#     data='/content/dataset/DatasetAug/data.yaml',
#     epochs=50,
#     imgsz=1024, 
#     lr0=0.0008, 
#     device=0,
#     batch=16, 
#     patience=15, 
#     augment=True,
#     mosaic=1.0, 
#     hsv_h=0.015, hsv_s=0.7, hsv_v=0.4,
#     fliplr=0.5,
# )