# -*- coding: utf-8 -*-
#pwm模式，以15号脚为例
import RPi.GPIO as GPIO
import time


#树莓派可能不止有一个脚本/电路在操纵GPIO, 如果树莓派检测到引脚不是默认的输入状态, 会给出警告, 可以用一行代码避免警告
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)

time.sleep(2)
p = GPIO.PWM(15, 80)
p.start(1)
p.ChangeFrequency(5)
time.sleep(5)
p.ChangeFrequency(70)
time.sleep(5)
p.stop()
GPIO.cleanup()
