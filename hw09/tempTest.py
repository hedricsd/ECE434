#!/usr/bin/python3
import os

temp1 = os.open("/sys/class/hwmon/hwmon0/temp1_input", os.O_RDONLY);
temp1Value = os.read(temp1, 6);
temp1Value = temp1Value.decode("utf-8")

temp2 = os.open("/sys/class/hwmon/hwmon1/temp1_input", os.O_RDONLY);
temp2Value = os.read(temp2, 6);
temp2Value = temp2Value.decode("utf-8")

temp3 = os.open("/sys/class/hwmon/hwmon2/temp1_input", os.O_RDONLY);
temp3Value = os.read(temp3, 6);
temp3Value = temp3Value.decode("utf-8")

print(int(temp1Value)/1000, int(temp2Value)/1000, int(temp3Value)/1000);