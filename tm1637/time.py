#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://raspberrytips.nl

import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637


dio=2
clk=3

Display = tm1637.TM1637(clk,dio,tm1637.BRIGHT_TYPICAL)

Display.Clear()
Display.SetBrightnes(7)

sig=14


#设置gpio的控制模式
GPIO.setmode(GPIO.BCM)
#避免警告
GPIO.setwarnings(False)
#设置2号脚为0v
GPIO.setup(sig,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#低电平触发可用GPIO.FALLING两者都触发可用GPIO.BOTH
GPIO.add_event_detect(sig, GPIO.RISING)

a=0
while a<1000:
# if GPIO.event_detected(sig):
     #设置4号脚为输出模式
   now = datetime.datetime.now()
   hour = now.hour
   minute = now.minute
   second = now.second
   currenttime = [ int(minute / 10), minute % 10, int(second / 10), second % 10 ]

   Display.Show(currenttime)
   Display.ShowDoublepoint(second % 2)

   time.sleep(1)
   a=a+1

Display.stop()
GPIO.cleanup()
