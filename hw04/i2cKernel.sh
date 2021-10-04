#!/bin/bash

while true; do

    cd /sys/class/i2c-adapter/i2c-2
    cd 2-0048/hwmon/hwmon0
    cat temp1_input
    echo "milli-degrees C"
done
