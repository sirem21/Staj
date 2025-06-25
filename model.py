from ultralytics import YOLO

class Model:
    def __init__(self,model = YOLO("yolo11n.pt") ):
        self.model = model
    def detect(self,frame):
        results = self.model(frame)
        annotated_frame = results[0].plot()
        return annotated_frame

