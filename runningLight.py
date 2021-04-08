import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
D = [24,25,8,7,12,16,20,21]
GPIO.setup(D, GPIO.OUT)

ledNumber = 

def runningLight(c, p):
    for i in range(c):
        GPIO.output(D[ledNumber],1)
        time.sleep(p)
        GPIO.output(D[ledNumber],0)
        if ledNumber<7:
            ledNumber=ledNumber+1
        else:
            ledNumber=ledNumber-7
 
c = 
p = 
runningLight(c, p)

GPIO.output(1,0)
GPIO.cleanup()