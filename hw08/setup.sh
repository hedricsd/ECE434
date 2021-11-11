# Author: Sam Hedrick

#////Blinking an LED/////
config-pin P9_31 gpio
echo out > /sys/class/gpio/gpio110/direction

#////PWM Generator/////
# config-pin P9_31 pruout

#////Controlling PWM Frequency/////
# config-pin P9_28 pruout
# config-pin P9_29 pruout
# config-pin P9_30 pruout
# config-pin P9_31 pruout