from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
try:
	i = 0
	while(True):
		sleep(5)
		camera.capture('{0}.jpg'.format(i))
		i+= 1
except KeyboardInterrupt:
	pass
camera.stop_preview()
