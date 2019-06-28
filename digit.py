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
#    dig2=21
#    dig1=20
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
#	print(nummbers[i])
    return




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
chan_list = [2,3,4,17,27,22,10,9]
GPIO.setup(chan_list, GPIO.OUT)


'''
1是关
GPIO.output(a,0)
GPIO.output(b,0)

'''
def printNumber (number1,number2):

 dig1=21
 dig2=20
 sleeptime=0.01
 GPIO.setup(dig1, GPIO.OUT)
 GPIO.setup(dig2, GPIO.OUT)

 i=0
 while i<25:
	GPIO.output(dig1,1)
	GPIO.output(dig2,0)
	showNumber(number1)
	time.sleep(sleeptime)
	GPIO.output(dig1,0)
	GPIO.output(dig2,1)
	showNumber(number2)
	time.sleep(sleeptime)
	GPIO.output(dig2,0)
	i=i+1

#读取并显示当前秒

def printNowSecond():
    curTime = time.localtime(time.time())
    curSecond = time.strftime("%S", curTime)
    splitTime = list(curSecond)
    printNumber(splitTime[0],splitTime[1])

i=0
while i<20 :
	printNowSecond()
	i=i+1
GPIO.cleanup()
