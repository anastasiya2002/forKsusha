import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
D = [21,20,16,12,7,8,25,24]
GPIO.setup(D, GPIO.OUT)

def blink(n, c, p):
    for i in (0, c-1):
        GPIO.output(D[n],1)
        time.sleep(p)
        GPIO.output(D[n],0)
        time.sleep(p)
blink(0, 3, 0.1)

GPIO.output(1,0)
GPIO.cleanup()