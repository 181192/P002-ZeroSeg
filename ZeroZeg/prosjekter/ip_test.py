#! /usr/bin/env python

import ZeroSeg.led as led
import time
from datetime import datetime
import RPi.GPIO as GPIO
import socket

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def getIp():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("gmail.com",80))
	ip = s.getsockname()[0]
	s.close()
	return ip

def writeIp(device, deviceId, min, max):
	text = getIp().split(".")
	resultat = text[min] + "." + text[max]
	device.write_text(0,resultat)

device = led.sevensegment()

checher = True

while checher:
	writeIp(device, 0, 0, 1)
	time.sleep(5)
	writeIp(device, 0, 2, 3)
	time.sleep(5)
	device.clear() 
