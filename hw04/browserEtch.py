#!/usr/bin/env python3 

import numpy as np
import smbus
from flask import Flask, render_template, request
app = Flask(__name__)

#Variables to create array
rows = 8
cols = 8
size = 8
curX = 0
curY = 0

matrix = 0x70
picture = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
bus = smbus.SMBus(2)   


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
def printMatrix():
    global rows, cols
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

@app.route("/")
def index():
    return render_template('indexOne.html')
    
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    global curX, curY, picture, array
    if action == "down":
        if curY < size-1:
            curY+=1
    if action == "up":
        if curY > 0:
            curY-=1
    if action == "left":
        if curX < size-1:
            curX+=1
    if action == "right":
        if curX > 0:
            curX-=1
    if action == "clear":
        array = clearArray(rows, cols, curX, curY)
    array[curX, curY] = 1
    printMatrix()
    return render_template('indexOne.html')
    
if __name__ == "__main__":
   app.run(port=8081, host='0.0.0.0', debug=True)