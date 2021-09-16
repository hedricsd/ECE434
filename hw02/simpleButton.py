import Adafruit_BBIO.GPIO as GPIO

# Declaring variables for GPIO pins for LEDS
led1 = "P9_11"
led2 = "P9_14"
led3 = "P9_13"
led4 = "P9_12"

# Declaring variables for GPIO pins for pushbuttons
pb1 = "P8_7"
pb2 = "P8_8"
pb3 = "P8_9"
pb4 = "P8_10"

# Counters used to determine whether LED is on or off in callback
counter1 = -1
counter2 = -1
counter3 = -1
counter4 = -1

# Setting up the pushbuttons as inputs
GPIO.setup(pb1, GPIO.IN)
GPIO.setup(pb2, GPIO.IN)
GPIO.setup(pb3, GPIO.IN)
GPIO.setup(pb4, GPIO.IN)

# Setting up the pushbuttons as outputs
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

# Callbacks that check the counter and set the LED either high or low
def callback1(channel):
    if(counter1 % 2 == 0):
        GPIO.output(led1, GPIO.HIGH)
    else:
        GPIO.output(led1, GPIO.LOW)
        
def callback2(channel):
    if(counter2 % 2 == 0):
        GPIO.output(led2, GPIO.HIGH)
    else:
        GPIO.output(led2, GPIO.LOW)
        
def callback3(channel):
    if(counter3 % 2 == 0):
        GPIO.output(led3, GPIO.HIGH)
    else:
        GPIO.output(led3, GPIO.LOW)
        
def callback4(channel):
    if(counter4 % 2 == 0):
        GPIO.output(led4, GPIO.HIGH)
    else:
        GPIO.output(led4, GPIO.LOW)

# Adding an event detection to each pushbutton on a falling edge that calls the callback
GPIO.add_event_detect(pb1, GPIO.FALLING, callback = callback1)
GPIO.add_event_detect(pb2, GPIO.FALLING, callback = callback2)
GPIO.add_event_detect(pb3, GPIO.FALLING, callback = callback3)
GPIO.add_event_detect(pb4, GPIO.FALLING, callback = callback4)

while(1):
    
    # if first push button is pressed, callback1 is called and counter1 is increased
    if(GPIO.event_detected(pb1)):
        #turn on led1
        counter1+=1
    
    # if second push button is pressed, callback2 is called and counter1 is increased    
    if(GPIO.event_detected(pb2)):
        #turn on led2
        counter2+=1
        
    # if third push button is pressed, callback3 is called and counter1 is increased
    if(GPIO.event_detected(pb3)):
        #turn on led3
        counter3+=1
        
    # if fourth push button is pressed, callback4 is called and counter1 is increased
    if(GPIO.event_detected(pb4)):
        #turn on led4
        counter4+=1


