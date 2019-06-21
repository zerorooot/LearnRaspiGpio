# -*- coding: utf-8 -*-
# 指定针脚输出，用来测定led灯的输出
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

chan_list = [2,4,17,27]
GPIO.setup(chan_list, GPIO.OUT)



GPIO.output(17,0)
GPIO.output(2,0)
GPIO.output(4,1)

#设置27针脚为pwm模式
#p = GPIO.PWM(channel, frequency)
p = GPIO.PWM(27, 80)
p.start(1)
p.ChangeFrequency(5)
time.sleep(5)
p.ChangeFrequency(70)
time.sleep(5)
p.stop()


time.sleep(2)
GPIO.cleanup()
