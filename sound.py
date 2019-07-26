# -*- coding: utf-8 -*-
#gpio输入模式demo
import RPi.GPIO as GPIO
import random
import time

pin=21

#设置gpio的控制模式
GPIO.setmode(GPIO.BCM)
#避免警告
GPIO.setwarnings(False)
#设置2号脚为0v
GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

chan_list = [4,17,22]
GPIO.setup(chan_list, GPIO.OUT)

b=-1
c=-1
d=-1

#低电平触发可用GPIO.FALLING两者都触发可用GPIO.BOTH
GPIO.add_event_detect(pin, GPIO.RISING)
while True:
 if GPIO.event_detected(pin):
        b=random.randint(0,1)
        c=random.randint(0,1)
        d=random.randint(0,1)
        GPIO.output(17,b)
        GPIO.output(4,c)
        GPIO.output(22,d)
	time.sleep(0.2)
GPIO.cleanup()
