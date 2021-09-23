#!/bin/bash

# Forever Loop that reads the temperature, converts to F, and prints the value
while true
do
    temp1=$(sudo i2cget -y 2 0x48)
    temp2=$(sudo i2cget -y 2 0x4a)
    
    temp3=$(( (temp1 *9)/5 +32))
    temp4=$(( (temp2 *9)/5 +32))
    echo "Top: $temp3 Bottom: $temp4"
    sleep 2
done