#!/usr/bin/python3

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

# Intiallizing the I2Cbus and temp sensors
bus = smbus.SMBus(2)
top = 0x48
bottom = 0x4a

#GPIO pins
topInt = "P8_4"
botInt = "P8_3"

#Setting Up GPIO pins
GPIO.setup(topInt, GPIO.IN)
GPIO.setup(botInt, GPIO.IN)


# Forever Loop that reads the temperature, converts to F, and prints the value
while(True):
    topTemp = bus.read_byte_data(top, 0)
    bottomTemp = bus.read_byte_data(bottom, 0)
    topTemp = topTemp*9/5 + 32
    bottomTemp = bottomTemp*9/5 + 32
    print("Top: %d    Bottom: %d" % (topTemp, bottomTemp))
    time.sleep(2)
    

