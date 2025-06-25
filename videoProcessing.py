import cv2
class VideoRead:
   def __init__(self,videoPath):
      self.path = videoPath
      self.cap = cv2.VideoCapture(self.path)

      if not self.cap.isOpened():
         raise ValueError(f"Video can't be opened: {self.path}")

   def openVideo(self):
      while True:
         ret, frame = self.cap.read()
         if not ret:
            break

         cv2.imshow("Webcam", frame)

         # click q for exit
         if cv2.waitKey(1) & 0xFF == ord("q"):
            break
      self.cap.release()
      cv2.destroyAllWindows()


if __name__ == '__main__':

   video = VideoRead("video3.mp4")
   video.openVideo()