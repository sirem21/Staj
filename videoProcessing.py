import cv2

def videoCapture(videoPath):
   try:
      video = cv2.VideoCapture(videoPath)
      return video
   except Exception as e:
      print(f"Error: {e}")
      exit()
      return None
   
def main():
   videoPath = "video3.mp4"
   video = videoCapture(videoPath)

   if video.isOpened():
      print("Video opened successfully.")
   else:
      print("Error opening video file.")
 

if __name__ == "__main__":
   main()



