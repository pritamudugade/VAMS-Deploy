from ultralytics import YOLO

# Load a model
model = YOLO(r"C:\Users\DELL\Downloads\new\person_new_best.pt")
# Use the model to detect objects
model.predict(source="rtsp://admin:admin12345@192.168.1.245:554/Streaming/Channels/701/",show=True, save=True, save_crop=True, save_txt=True)