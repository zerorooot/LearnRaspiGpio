import RPi.GPIO as GPIO
import time

Trig_Pin = 20
Echo_Pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig_Pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Echo_Pin, GPIO.IN)

#time.sleep(2)

def checkdist():
    #发出触发信号
    GPIO.output(Trig_Pin, GPIO.HIGH)
    #保持10us以上
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    #发现高电平时开时计时
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    #高电平结束停止计时
    t2 = time.time()
    #返回距离，单位为米
    return (t2-t1)*340*100/2

try:
    while True:
        print 'Distance:%0.2f cm' % checkdist()
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
