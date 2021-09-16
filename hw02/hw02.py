#!/usr/bin/env python3 

import numpy as np
import Adafruit_BBIO.GPIO as GPIO

# Function that clears/sets up the array while keeping the current X and current Y value the same
def clearArray(rows, cols, curX, curY):
    array = np.empty([rows, cols], dtype = object)

    for a in range(rows):
        for b in range(cols):
            array[a, b] = '  '
    
    for a in range(size):
        array[0][a + 2] = str(a).zfill(2) # zfill makes the array values all have 2 spaces so the format looks nicer
    for b in range(size):
        array[b + 1][0] = str(b).zfill(2)
        array[b + 1][1] = ':'
    array[curX, curY] = " X"
    return array
    
# Function that goes through the numpy array and prints it in an easier to understand format
def printMatrix(a):
    rows = a.shape[0]
    cols = a.shape[1]
    for i in range(0,rows):
        for j in range(0,cols):
            print("%s" %a[i,j], end = ' ') # end = ' ' makes it so it prints the array rows on one line
        print()

# Variable that I use to create array
size = int(input("Enter a Matrix Size: "))
rows = size + 1
cols = size + 2
curX = 1
curY = 2

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
    #detects up movement
    if(GPIO.event_detected(pb1)):
        if(curX > 1):
            curX-=1
        array[curX, curY] = " X" # prints an 'X' where the etch a sketch moves
        printMatrix(array) # reprints the new updated matrix
    
    # detects left movement   
    if(GPIO.event_detected(pb2)):
        if(curY > 2):
            curY-=1
        array[curX, curY] = " X" # prints an 'X' where the etch a sketch moves
        printMatrix(array) # reprints the new updated matrix
        
    # detects right movement
    if(GPIO.event_detected(pb3)):
        if(curY < size + 1):
            curY+=1
        array[curX, curY] = " X" # prints an 'X' where the etch a sketch moves
        printMatrix(array) # reprints the new updated matrix
        
    # detects down movement
    if(GPIO.event_detected(pb4)):
        if(curX < size):
            curX+=1
        array[curX, curY] = " X" # prints an 'X' where the etch a sketch moves
        printMatrix(array) # reprints the new updated matrix
    