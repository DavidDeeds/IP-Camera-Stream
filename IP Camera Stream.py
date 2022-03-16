import cv2
import imutils

from imutils.video import VideoStream

#Set your cameras username, password and IP address parameters below
#Note this string is tested workign with Hikvision, you might have to change slightly for other brands
IPCamera_url = "rtsp://username:password@192.168.1.1:554/Streaming/Channels/101"

video_stream = VideoStream(IPCamera_url).start()

while True:
    frame = video_stream.read()
    if frame is None:
        continue
    
    #Set window size otherwise it may span outside of monitor boundries
    frame = imutils.resize(frame,width=800)
    
    #Spawn window to display stream
    cv2.imshow('My Camera Name', frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    #Press letter q to quit window
    if key == ord('q'):
        break

cv2.destroyAllWindows()
video_stream.stop()