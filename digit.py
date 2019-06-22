# -*- coding: utf-8 -*-
# 指定针脚输出，用来测定led灯的输出
import RPi.GPIO as GPIO
import time

def showNumber (nummber) :
    a = 2
    b = 3
    c = 4
    d = 17
    e = 27
    f = 22
    g = 10
    dp = 9
    trans = {'0': [a, f, e, d, c, b], '1': [b, c], '2': [a, b, g, e, d], '3': [a, b, g, c, d], '4': [f, g, b, c],
             '5': [a, f, g, c, d], '6': [a, f, g, e, c, d], '7': [a, b, c], '8': [a, f, b, g, e, c, d],
             '9': [a, f, b, g, c, d]}

#    trans = {'0': [g], '1': [a,d,e,f,g], '2': [c,f],'3': [e,f],'4': [a,e,d],'5': [b,e],'6': [b],'7': [f,g,e,d],'8': [],'9': [e]}

#关闭所有灯
    chan_list = [2,3,4,17,27,22,10,9]
    for i in range(len(chan_list)):
	 GPIO.output(chan_list[i],1)
#开灯
    nummbers=trans[nummber]
    for i in range(len(nummbers)):
        GPIO.output(nummbers[i], 0)
	print(nummbers[i])
    return




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
chan_list = [2,3,4,17,27,22,10,9]
GPIO.setup(chan_list, GPIO.OUT)


'''
1是关
GPIO.output(a,0)
GPIO.output(b,0)
GPIO.output(c,0)
GPIO.output(d,0)
GPIO.output(e,0)
GPIO.output(f,0)
GPIO.output(g,1)
GPIO.output(dp,0)

'''


showNumber('6')

time.sleep(2)
GPIO.cleanup()
