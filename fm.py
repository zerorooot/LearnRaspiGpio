# -*- coding: utf-8 -*-
#控制蜂鸣器
import RPi.GPIO as GPIO

import time

#设置gpio的控制模式
GPIO.setmode(GPIO.BCM)
#避免警告
GPIO.setwarnings(False)
#设置15号脚为输出模式
GPIO.setup(4, GPIO.OUT)
#也可以用0或1来代替True和False
GPIO.output(4,1)
time.sleep(2)
GPIO.output(4,0)
GPIO.cleanup()
