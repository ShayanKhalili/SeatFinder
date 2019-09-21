from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
try:
	while(True):
		camera.capture('.?
camera.stop_preview()
