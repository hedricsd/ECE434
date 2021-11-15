#test

import Adafruit_BBIO.GPIO as GPIO
from time import sleep

sensor = "P9_13"
buzzer = "P9_11"

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

while True:
    if GPIO.input(sensor): # 1 is object not detected
        GPIO.output(buzzer, GPIO.LOW)
    else:
        GPIO.output(buzzer, GPIO.HIGH)
        print("Buckets!!")
        sleep(0.5)