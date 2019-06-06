# GPIO Outputs

1. First set up RPi.GPIO (as described [here](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/))

```
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
```

2. To set an output high:

```
GPIO.output(12, GPIO.HIGH)
 # or
GPIO.output(12, 1)
 # or
GPIO.output(12, True)
```

3. To set an output low:

```
GPIO.output(12, GPIO.LOW)
 # or
GPIO.output(12, 0)
 # or
GPIO.output(12, False)
```

4. To output to several channels at the same time:

```
chan_list = (11,12)
GPIO.output(chan_list, GPIO.LOW) # all LOW
GPIO.output(chan_list, (GPIO.HIGH,GPIO.LOW))  # first LOW, second HIGH
```

5. Clean up at the end of your program

```
GPIO.cleanup()
```

Note that you can read the current state of a channel set up as an output using the input() function. For example to toggle an output:

```
GPIO.output(12, not GPIO.input(12))
```
