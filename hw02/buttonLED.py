#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

LED   = "P9_11"
delay = 1

GPIO.setup(LED, GPIO.OUT)

while True:
    GPIO.output(LED, 1)
    time.sleep(delay)
    GPIO.output(LED, 0)
    time.sleep(delay)
