#!/usr/bin/python3

from mmap import mmap
import time, struct
import Adafruit_BBIO.GPIO as GPIO

# Port Addresses
GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
greenLED = 1<<27
blueLED = 1<<18

pb1 = "P8_8"
pb2 = "P8_7"
GPIO.setup(pb1, GPIO.IN)
GPIO.setup(pb2, GPIO.IN)
GPIO.add_event_detect(pb1, GPIO.FALLING)
GPIO.add_event_detect(pb2, GPIO.FALLING)
pb1_on = 0
pb2_on = 0

# Next we need to make the mmap, using the desired size and offset:
with open("/dev/mem", "r+b" ) as f:
  mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)


packed_reg = mem[GPIO_OE:GPIO_OE+4]

reg_status = struct.unpack("<L", packed_reg)[0]

reg_status &= ~(greenLED)
reg_status &= ~(blueLED)

mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

# 7and 8
while(True):
    if(GPIO.event_detected(pb1)):
      if(pb1_on == 0):
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", greenLED)
        pb1_on = 1
      else:
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", greenLED)
        pb1_on =0
      
    if(GPIO.event_detected(pb2)):
      if(pb2_on == 0):
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", blueLED)
        pb2_on = 1
      else:
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", blueLED)
        pb2_on = 0