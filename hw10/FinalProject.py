#////////////////////////////////
# Author: Sam Hedrick and Tristen Foisy
# Date: 11/15/2021
# Purpose: This is our final project for ECE434 Embedded Linux
#////////////////////////////////

# These are the imported libraries that are needed for our code
import Adafruit_BBIO.GPIO as GPIO
from time import sleep
import Adafruit_BBIO.PWM as PWM
import math

# Naming all of our ports that our componenets use
sensor = "P9_13"
buzzer = "P9_11"
button = "P9_41"
servo= "P9_14" 
segments = ("P9_42", "P9_31", "P9_29", "P9_28", "P9_27", "P9_26", "P9_25", "P9_30")
digits = ("P9_21", "P9_22", "P9_23", "P9_24")

# For the 7 segment display we initialize all of the segments off
for seg in segments:
    GPIO.setup(seg, GPIO.OUT)
    GPIO.output(seg, 0)
    
# For the 7 segment display, having the digits high is having them not display anything
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)
 
# Dict of our servo angles so we can call the difference in the score and have the right angle value
servo_angle = {'-4':180,
    '-3':160,
    '-2':140,
    '-1':120,
    '0':100,
    '1':80,
    '2':60,
    '3':40,
    '4':20}
    
# Dict of our 7 segment display numbers for each number 0-9
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
    
# Variables used by our servo motor
duty_min = 3
duty_max = 14.5
duty_span = duty_max - duty_min

# Initiallizes the servo and sets the servo to the middle position
PWM.start(servo, (100-duty_min), 60.0, 1)
duty = 100 - ((100.0/ 180) * duty_span + duty_min) 
PWM.set_duty_cycle(servo, duty)

# Setting up GPIO pins ans inputs and outputs
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

totalA=0        # variable for the total running count of A
totalB=0        # variable for the total running count of B
currentA=0      # variable for the total of A for a current round
currentB=0      # variable for the total of B for a current round
current=0       # variable for the current player. 0 is A, 1 is B
totalThrows = 0 # variable for the total number of throws in a round
madeTurn = 0    # variable to make sure only one make happens per turn

# Adding a GPIO event detect for when the button is pressed.
GPIO.add_event_detect(button, GPIO.FALLING)

#try/finally statement so that we can exit with a cleanup

try:
    while True:
        # Sets the 7 segment display up, turning on the first digit and then going through the number from the running score
        GPIO.output(digits[0], 0)
        GPIO.output(digits[1], 1)
        GPIO.output(digits[2], 1)
        GPIO.output(digits[3], 1)
        i = 0
        for val in num[str(math.trunc(totalA/10))]: # first digit of total A
            GPIO.output(segments[i], val)
            i+=1
        i = 0
        sleep(0.0065) # sleep to reduce jitter
        
        # Sets the 7 segment display up, turning on the second digit and then going through the number from the running score
        GPIO.output(digits[0], 1)
        GPIO.output(digits[1], 0)
        GPIO.output(digits[2], 1)
        GPIO.output(digits[3], 1)
        for val in num[str(totalA%10)]: # second digit of total A
            GPIO.output(segments[i], val)
            i+=1
        i = 0
        sleep(0.0065) # sleep to reduce jitter
        
        # Sets the 7 segment display up, turning on the third digit and then going through the number from the running score
        GPIO.output(digits[0], 1)
        GPIO.output(digits[1], 1)
        GPIO.output(digits[2], 0)
        GPIO.output(digits[3], 1)
        for val in num[str(math.trunc(totalB/10))]: # first digit of total B
            GPIO.output(segments[i], val)
            i+=1
        i = 0
        sleep(0.0065) #sleep to reduce jitter
        
        # Sets the 7 segment display up, turning on the fourth digit and then going through the number from the running score
        GPIO.output(digits[0], 1)
        GPIO.output(digits[1], 1)
        GPIO.output(digits[2], 1)
        GPIO.output(digits[3], 0)
        for val in num[str(totalB%10)]: #second digit of total B
            GPIO.output(segments[i], val)
            i+=1
        sleep(0.0065) # sleep to reduce jitter
    
        # Detects when the button is pressed
        if(GPIO.event_detected(button)):
            sleep(.1) 
            madeTurn = 0 # Resets to 0 since it is a new turn
            current = (current+1)%2 # changes current to opposite number to change players
            totalThrows +=1 # increases the total throws
            print(totalThrows,"/8 throws done") # prints the number of throws done
            
            # loop needed for change of round
            if(totalThrows == 8):
                print("Round Over!")
                
                # calculates which player had more points and adds to their total
                if(currentA > currentB):
                    totalA+= currentA-currentB
                elif(currentB > currentA):
                    totalB+= currentB-currentA
                    
                print("A: ", totalA, " B: ", totalB)
                
                # Game is won at 21. Prints which player wins
                if(totalA >=21):
                    print("Game Over! Player A wins!!")
                    exit()
                if(totalB >=21):
                    print("Game Over! Player B wins!!")
                    exit()
                    
                totalThrows = 0 # resets the totalThrows for the new round
                currentA = 0 # Resets currentA for the new round
                currentB = 0 # Resets currentB for the new round
                duty = 100 - ((100.0/ 180) * duty_span + duty_min) # Resets the servo
                PWM.set_duty_cycle(servo, duty)
                
        # Turns off buzzer when nothing is detected
        if GPIO.input(sensor): # 1 is object not detected
            GPIO.output(buzzer, GPIO.LOW)
            
        # If IR senses something
        else:
            if(madeTurn ==0): # makes sure that only one shot is made per throw
                if(current == 0):
                    currentA+=1 # if playerA's turn adds to their total
                else:
                    currentB+=1 # if playerB's turn adds to their total
                GPIO.output(buzzer, GPIO.HIGH) # turns on buzzer
                print("Cornhole!!")
                sleep(0.5)
                angle_f = servo_angle[str(currentB-currentA)] # sets servo to desired angle
                duty = 100 - ((angle_f / 180) * duty_span + duty_min) 
                PWM.set_duty_cycle(servo, duty)
                madeTurn = 1 # toggles variable

# cleans up GPIO and PWM after code finishes
finally:
    print("Thanks for playing!")
    GPIO.output(buzzer, GPIO.LOW)
    GPIO.cleanup()
    PWM.stop(servo)
    PWM.cleanup()

