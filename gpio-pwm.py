#pwm
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
time.sleep(2)
p = GPIO.PWM(15, 80)
p.start(1)
p.ChangeFrequency(5)
time.sleep(5)
p.ChangeFrequency(70)
time.sleep(5)
p.stop()
GPIO.cleanup()
