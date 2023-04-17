from ultralytics import YOLO

# Load a model
model = YOLO("/home/sparklab/ultralytics/ultralytics/models/v8/yolov8n.yaml")  # build a new model from scratch
# model = YOLO("/home/sparklab/yolov8_tracking/weights/bestN.pt")
# model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
# model = YOLO("/home/sparklab/yolov8_tracking/weights/best.pt")
# model = YOLO ("/home/sparklab/ultralytics/ultralytics/models/v8/yolov8n.yaml").load("/home/sparklab/yolov8_tracking/weights/yolov8n.pt")
# model = YOLO ("/home/sparklab/yolov8_tracking/runs/detect/train107/weights/last.pt")
# Use the model
model.train(data="/home/sparklab/dogs2014/dataset1.yaml", epochs = 500, batch = 72, save_period = 5, workers = 20,
             resume = True)

# model.train(data="/home/sparklab/dogs2014/dataset1.yaml", epochs = 150, batch = 72, lr0 = 0.0005) #fine-tune
# model.train(data="/home/sparklab/dogs2014/dataset.yaml", epochs=50, batch = 24) # yolov8m
metrics = model.val(data="/home/sparklab/dogs2014/dataset1.yaml", split = "train")  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# success = model.export()  # export the model to ONNX format
