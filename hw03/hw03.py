#!/usr/bin/env python3 

import numpy as np
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus


# Variable that I use to create array
rows = 8
cols = 8
size = 8
curX = 0
curY = 0

# Variables used in LED matrix and Temp sensors
matrix = 0x70
picture = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
bus = smbus.SMBus(2)   
top = 0x48
bottom = 0x4a

# Prints the first original matrix
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# Function that clears/sets up the array while keeping the current X and current Y value the same
def clearArray(rows, cols, curX, curY):
    array = np.empty([rows, cols])

    for a in range(rows):
        for b in range(cols):
            array[a, b] = 0
    array[curX, curY] = 1
    return array
    
# Function that takes array and prints into LED matrix
def printMatrix(a):
    rows = a.shape[0]
    cols = a.shape[1]
    for i in range(0,rows):
        total = 0; # Initiallizing the total for the LED values
        for j in range(0,cols):
            if(array[i, j] == 1): #Checks values to see if on
                total+=2**j # If on, adds the value to a running sum that is the decimal represntation of LEDs on
            picture[i*2] = total # Sets column to running total
        picture[i*2 + 1] = 0 # Resets all red LEDS to off
    picture[curX*2 + 1] = 2 ** curY # Turns on the red LED at curX, curY
    bus.write_i2c_block_data(matrix, 0, picture)


# Initiallizing array
array = clearArray(rows, cols, curX, curY)

# Prints the first original matrix
printMatrix(array)

# Declaring variables for GPIO pins for pushbuttons
pb1 = "P8_7"
pb2 = "P8_8"
pb3 = "P8_9"
pb4 = "P8_10"

# Setting up the pushbuttons as inputs
GPIO.setup(pb1, GPIO.IN)
GPIO.setup(pb2, GPIO.IN)
GPIO.setup(pb3, GPIO.IN)
GPIO.setup(pb4, GPIO.IN)


# Adding an event detection to each pushbutton on a falling edge that calls the callback
GPIO.add_event_detect(pb1, GPIO.FALLING)
GPIO.add_event_detect(pb2, GPIO.FALLING)
GPIO.add_event_detect(pb3, GPIO.FALLING)
GPIO.add_event_detect(pb4, GPIO.FALLING)

while(1):
    # Getting the temperature values
    topTemp = bus.read_byte_data(top, 0)
    bottomTemp = bus.read_byte_data(bottom, 0)
    topTemp = topTemp*9/5 + 32
    bottomTemp = bottomTemp*9/5 + 32
    
    # If the top temperature sensor is too high, LED goes all Red
    if(topTemp > 79.5):
        picture = [0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF,
    0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF]
        bus.write_i2c_block_data(matrix, 0, picture)
        print("OVERHEATING!!! Please Reset.")
    # If the bottom temperature sensor is too high, LED matrix resets
    if(bottomTemp > 79.5):
        print("Resetting")
        array = clearArray(rows, cols, curX, curY)
        printMatrix(array)

    # detects up movement
    if(GPIO.event_detected(pb1)):
        if(curX < size - 1):
            curX+=1
        array[curX, curY] = 1 # sets matrix value to 1 where the etch a sketch moves
        printMatrix(array) # reprints the new updated matrix
        
    # detects left movement
    if(GPIO.event_detected(pb2)):
        if(curY < size - 1):
            curY+=1
        array[curX, curY] = 1 # sets matrix value to 1 where the etch a sketch moves
        printMatrix(array) # reprints the new updated matrix
    
    # detects right movement   
    if(GPIO.event_detected(pb3)):
        if(curY > 0):
            curY-=1
        array[curX, curY] = 1 # sets matrix value to 1 where the etch a sketch moves
        printMatrix(array) # reprints the new updated matrix
        
    #detects down movement
    if(GPIO.event_detected(pb4)):
        if(curX > 0):
            curX-=1
        array[curX, curY] = 1 # sets matrix value to 1 where the etch a sketch moves
        printMatrix(array) # reprints the new updated matrix