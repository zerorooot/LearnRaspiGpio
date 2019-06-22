# -*- coding: utf-8 -*-
# demo程序
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

chan_list = [17,27]
GPIO.setup(chan_list, GPIO.OUT)

GPIO.output(17,0)
GPIO.output(27,1)
time.sleep(2)
GPIO.cleanup()
