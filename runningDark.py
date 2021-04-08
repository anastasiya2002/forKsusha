import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
D = [24,25,8,7,12,16,20,21]
GPIO.setup(D, GPIO.OUT)

GPIO.output(D[0],1)
GPIO.output(D[1],1)
GPIO.output(D[2],1)
GPIO.output(D[3],1)
GPIO.output(D[4],1)
GPIO.output(D[5],1)
GPIO.output(D[6],1)
GPIO.output(D[7],1)

ledNumber = 

def runningDark(c, p):
    for i in range(c):
        GPIO.output(D[ledNumber],0)
        time.sleep(p)
        GPIO.output(D[ledNumber],1)
        if ledNumber<7:
            ledNumber=ledNumber+1
        else:
            ledNumber=ledNumber-7
 
c = 
p = 
runningLight(c, p)

GPIO.output(1,0)
GPIO.cleanup()