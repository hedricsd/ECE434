import Adafruit_BBIO.GPIO as GPIO

button = "P9_12"
GPIO.setup(button, GPIO.OUT)


while(1):
   GPIO.output(button, GPIO.HIGH)
   GPIO.output(button, GPIO.LOW)
