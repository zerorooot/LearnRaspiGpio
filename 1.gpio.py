# -*- coding: utf-8 -*-
#gpio
import RPi.GPIO as GPIO

import time

#设置gpio的控制模式
GPIO.setmode(GPIO.BCM)
#避免警告
GPIO.setwarnings(False)
#设置15号脚为输出模式
GPIO.setup(15, GPIO.OUT)
#也可以用0或1来代替True和False
GPIO.output(15,True)
time.sleep(2)
GPIO.output(15,False)
GPIO.cleanup()
