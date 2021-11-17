#test

import Adafruit_BBIO.GPIO as GPIO
from time import sleep
import Adafruit_BBIO.PWM as PWM
import math

sensor = "P9_13"
buzzer = "P9_11"
button = "P9_41"
servo= "P9_14"
segments = ("P9_42", "P9_31", "P9_29", "P9_28", "P9_27", "P9_26", "P9_25", "P9_30")
digits = ("P9_21", "P9_22", "P9_23", "P9_24")

for seg in segments:
    GPIO.setup(seg, GPIO.OUT)
    GPIO.output(seg, 0)
    
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

servo_angle = {'-4':180,
    '-3':160,
    '-2':140,
    '-1':120,
    '0':100,
    '1':80,
    '2':60,
    '3':40,
    '4':20}

    
duty_min = 3
duty_max = 14.5
duty_span = duty_max - duty_min

PWM.start(servo, (100-duty_min), 60.0, 1)
duty = 100 - ((100.0/ 180) * duty_span + duty_min) 
PWM.set_duty_cycle(servo, duty)

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

totalA=0
totalB=0
currentA=0
currentB=0
current=0
totalThrows = 0
GPIO.add_event_detect(button, GPIO.FALLING)

try:
    while True:
        

        if(GPIO.event_detected(button)):
            sleep(.1)
            current = (current+1)%2
            totalThrows +=1
            print(totalThrows,"/8 throws done")
            if(totalThrows == 8):
                print("Round Over!")
                if(currentA > currentB):
                    totalA+= currentA-currentB
                elif(currentB > currentA):
                    totalB+= currentB-currentA
                print("A: ", totalA, " B: ", totalB)
                if(totalA >=21):
                    print("Game Over! Player A wins!!")
                    exit()
                if(totalB >=21):
                    print("Game Over! Player B wins!!")
                    exit()
                totalThrows = 0
                currentA = 0
                currentB = 0
                duty = 100 - ((100.0/ 180) * duty_span + duty_min) 
                PWM.set_duty_cycle(servo, duty)
                
                
            
        if GPIO.input(sensor): # 1 is object not detected
            GPIO.output(buzzer, GPIO.LOW)
        else:
            if(current == 0):
                currentA+=1
            else:
                currentB+=1
            GPIO.output(buzzer, GPIO.HIGH)
            print("Buckets!!")
            sleep(1)
            angle_f = servo_angle[str(currentB-currentA)]
            duty = 100 - ((angle_f / 180) * duty_span + duty_min) 
            PWM.set_duty_cycle(servo, duty)
finally:
    print("Thanks for playing!")
    GPIO.cleanup()
    PWM.stop(servo)
    PWM.cleanup()
