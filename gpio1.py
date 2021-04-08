import RPi.GPIO as GPIO
import time

a = 21
b = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(a, GPIO.OUT)
while True:
    GPIO.output(a,1)
    time.sleep(1)
    GPIO.output(a,0)
    time.sleep(1)


GPIO.output(a,0)
GPIO.cleanup()