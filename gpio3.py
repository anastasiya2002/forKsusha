import RPi.GPIO as GPIO
import time

bit_depth = 8
def bin_convert(n):
    N = bit_depth - 1
    p = 0
    X = []
    while N>0:
        p = int(n/2**N)
        if p==1:
            X.append(1)
            n-=2**N
        else:
            X.append(0)
        N-=1
    X.append(n)
    return X
print(bin_convert(2))

GPIO.setmode(GPIO.BCM)
D = [21,20,16,12,7,8,25,24]
GPIO.setup(D, GPIO.OUT)

for j in range(0,255):
    N = [0,0,0,0,0,0,0,0]
    N = bin_convert(j)
    print(N)
    for i in (bit_depth-1,0):  
       GPIO.output(D[i],N[i])
    time.sleep(0.3)
    
GPIO.output(D[i],0)
GPIO.cleanup()