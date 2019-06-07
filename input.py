# -*- coding: utf-8 -*-
#gpio输入模式demo
import RPi.GPIO as GPIO

import time

#设置gpio的控制模式
GPIO.setmode(GPIO.BCM)
#避免警告
GPIO.setwarnings(False)
#设置2号脚为0v
GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

a=0
while a<10:
 a=a+1
 if GPIO.input(channel):
  print('Input was HIGH')
 else:
  print('Input was LOW')

GPIO.cleanup()
