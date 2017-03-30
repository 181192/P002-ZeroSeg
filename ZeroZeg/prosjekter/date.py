#! /usr/bin/env python

import ZeroSeg.led as led
import time
import random
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setwarnings(False)

switch1 = 17
switch2 = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)

def date(device, deviceId):
	now = datetime.now()
	day = now.day
	month = now.month
	year = now.year - 2000

	dt = "%02d-%02d-%02d" % (day, month, year)
	device.write_text(deviceId, dt)

device = led.sevensegment()

checker = True

while checker:
	date(device, 0)
        time.sleep(0.2)
        device.clear()

	if not  GPIO.input(switch1):
		print "Bryter en trykket"
		text = led.sevensegment(cascaded = 2)
		text.write_text(1,"BYE")
		time.sleep(2)
		text.clear()
		checker = False
	elif not GPIO.input(switch2):
		print "Bryter to trykket"
		checker = False
