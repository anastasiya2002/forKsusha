import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
D = [24,25,8,7,12,16,20,21]
GPIO.setup(D, GPIO.OUT)

def decToBinList(N):
    a = bin(N)
    b = a[2::]
    print(b)
    number = list(b)
    c = len(number)
    for i in range (8-c):
        number.insert(i, '0')
    print(number)
N = 
decToBinList(N) 