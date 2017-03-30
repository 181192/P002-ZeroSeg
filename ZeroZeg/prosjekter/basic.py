import ZeroSeg.led as led
import time
import RPi.GPIO as GPIO

button1 = 17
button2 = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(button1, GPIO.IN)

button = True
while button:
	if not GPIO.input(button1):
		button = False
		print "Button 1 presset"
	else:	
		device = led.sevensegment(cascaded = 2)
		device.show_message("SEND NUDES", delay=0.5)
	

device.clear()
