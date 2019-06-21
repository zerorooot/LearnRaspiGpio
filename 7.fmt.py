# -*- coding: utf-8 -*-
#触摸器控制蜂鸣器
import RPi.GPIO as GPIO

import time

#设置gpio的控制模式
GPIO.setmode(GPIO.BCM)
#避免警告
GPIO.setwarnings(False)
#设置2号脚为0v
GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#低电平触发可用GPIO.FALLING两者都触发可用GPIO.BOTH
GPIO.add_event_detect(2, GPIO.RISING)

a=0
while a<10:
 if GPIO.event_detected(2):
     #设置4号脚为输出模式
   GPIO.setup(4, GPIO.OUT)
   GPIO.output(4,1)
   time.sleep(0.1)
   GPIO.output(4,0)
   print('Button pressed')
   a=a+1

GPIO.cleanup()
