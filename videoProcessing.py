

import cv2

videoPath = "video3.mp4"
def videoCapture(videoPath):
   try:
      video = cv2.VideoCapture(videoPath)
      return video

   except Exception as e:
      print(f"Error: {e}")
      exit()
      return None

video = videoCapture(videoPath)

while True:
   ret, frame = video.read()
   if not ret:
       break

   cv2.imshow("Webcam", frame)

   if cv2.waitKey(1) & 0xFF == ord("q"):
       break
   
   #click q for exit
