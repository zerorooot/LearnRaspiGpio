# -*- coding: utf-8 -*-
#心跳传感器控制灯亮灭
#pin2为心跳传感器的sig，用导线将心跳传感器的h正负极与led灯的正负极连接，pin21接led灯的另一个脚
import RPi.GPIO as GPIO
import random
import time

pin=2

#设置gpio的控制模式
GPIO.setmode(GPIO.BCM)
#避免警告
GPIO.setwarnings(False)
#设置2号脚为0v
GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN

#低电平触发可用GPIO.FALLING两者都触发可用GPIO.BOTH

#GPIO.add_event_detect(pin, GPIO.RISING)
GPIO.add_event_detect(pin, GPIO.FALLING)

GPIO.setup(21, GPIO.OUT)

while True:
 if GPIO.event_detected(pin):
	#查看是否心跳传感器有效
	print('Button pressed'+str(random.randint(0,1000)))
	GPIO.output(21,0)
	time.sleep(0.2)
	GPIO.output(21,1)

GPIO.cleanup()
