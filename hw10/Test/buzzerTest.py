# test
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

buzzer = "P9_11"
GPIO.setup(buzzer, GPIO.OUT)

while(True):
    GPIO.output(buzzer, GPIO.HIGH)
    sleep(1)
    GPIO.output(buzzer, GPIO.LOW)
    sleep(1)