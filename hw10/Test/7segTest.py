#test

import Adafruit_BBIO.GPIO as GPIO
import time

segments = ("P9_42", "P9_31", "P9_29", "P9_28", "P9_27", "P9_26", "P9_25", "P9_30")
digits = ("P9_21", "P9_22", "P9_23", "P9_24")

for seg in segments:
    GPIO.setup(seg, GPIO.OUT)
    GPIO.output(seg, 0)
    
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 0)
    

num = {'0':(1,0,1,0,1,1,1,1),
    '1':(0,0,1,0,1,0,0,0),
    '2':(1,0,0,1,1,0,1,1),
    '3':(0,0,1,1,1,0,1,1),
    '4':(0,0,1,1,1,1,0,0),
    '5':(0,0,1,1,0,1,1,1),
    '6':(1,0,1,1,0,1,1,1),
    '7':(0,0,1,0,1,0,1,0),
    '8':(1,0,1,1,1,1,1,1),
    '9':(0,0,1,1,1,1,1,1)}
    
i = 0
for total in num:
    for val in num[total]:
        GPIO.output(segments[i], val)
        i+=1
    i = 0
    time.sleep(1)
    
GPIO.cleanup()
    