import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
D = [21,20,16,12,7,8,25,24]
GPIO.setup(D, GPIO.OUT)

def lightUp(n, p):
    GPIO.output(D[n],1)
    time.sleep(p)
    GPIO.output(D[n],0)
lightUp(4,2)

GPIO.output(1,0)
GPIO.cleanup()