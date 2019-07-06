# -*- coding: utf-8 -*-
#触摸器控制蜂鸣器
import RPi.GPIO as GPIO

import time

sig=14
dio=2
clk=3



#设置gpio的控制模式
GPIO.setmode(GPIO.BCM)
#避免警告
GPIO.setwarnings(False)
#设置2号脚为0v
GPIO.setup(sig,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#低电平触发可用GPIO.FALLING两者都触发可用GPIO.BOTH
GPIO.add_event_detect(sig, GPIO.RISING)

a=0
while a<10:
 if GPIO.event_detected(sig):
     #设置4号脚为输出模式
   print('Button pressed')
   a=a+1

GPIO.cleanup()
