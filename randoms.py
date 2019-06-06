import RPi.GPIO as GPIO
import random
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.output(4,1)

a=0
b=-1
c=-1
d=-1
while a<10:
        b=random.randint(0,1)
        c=random.randint(0,1)
        d=random.randint(0,1)
        a=a+1
        GPIO.output(17,b)
        GPIO.output(27,c)
        GPIO.output(2,d)
        time.sleep(2)
        print("17:"+str(b)+"  27:"+str(c)+"  2:"+str(d))
GPIO.cleanup()
