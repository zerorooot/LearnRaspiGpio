
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(17,0)
GPIO.output(27,0)
GPIO.output(2,0)
GPIO.output(4,1)
time.sleep(2)
GPIO.cleanup()
