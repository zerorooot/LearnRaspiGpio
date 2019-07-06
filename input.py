# -*- coding: utf-8 -*-
#gpio输入模式demo
import RPi.GPIO as GPIO

import time

pin=2

#设置gpio的控制模式
GPIO.setmode(GPIO.BCM)
#避免警告
GPIO.setwarnings(False)
#设置2号脚为0v
GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

'''
查看2脚状态
 if GPIO.input(2):
  print('Input was HIGH')
 else:
  print('Input was LOW')
'''
#低电平触发可用GPIO.FALLING两者都触发可用GPIO.BOTH
GPIO.add_event_detect(pin, GPIO.RISING)
while True:
 if GPIO.event_detected(pin):
     print('Button pressed')

GPIO.cleanup()
