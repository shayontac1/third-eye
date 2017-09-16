#importing packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

#sleep to boot up
time.sleep(0.1)

#capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="jpeg", use_video_port = True):
	image= frame.array

	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF

	rawCapture.truncate(0)

	if key == ord("q"):
		break
