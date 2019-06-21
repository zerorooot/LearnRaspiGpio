# -*- coding: utf-8 -*-
#gpio输入模式demo
import RPi.GPIO as GPIO
import random
import time

#设置gpio的控制模式
GPIO.setmode(GPIO.BCM)
#避免警告
GPIO.setwarnings(False)
#设置2号脚为0v
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#低电平触发可用GPIO.FALLING两者都触发可用GPIO.BOTH
GPIO.add_event_detect(21, GPIO.RISING)

chan_list = [2,4,17,27]
GPIO.setup(chan_list, GPIO.OUT)
GPIO.output(4,1)
b=-1
c=-1
d=-1

while True:
 if GPIO.event_detected(21):
        b=random.randint(0,1)
        c=random.randint(0,1)
        d=random.randint(0,1)
	if b+c+d==3:
		continue
	print("17:"+str(b)+"  27:"+str(c)+"  2:"+str(d))
        GPIO.output(17,b)
        GPIO.output(27,c)
        GPIO.output(2,d)

GPIO.cleanup()
