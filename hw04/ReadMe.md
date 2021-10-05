# hw04
- Memory Map
- GPIO via mmap
- i2c via the Kernel Driver
- Control the LED matrix from a browser

## Memory Map
I attached my memory map that I created as MemoryMap.png

## GPIO via mmap
buttonLED.py covers the first part. This code reads from two switches to control 2 LEDs
mmapGPIO.py is the file for the second part of this section. mmapGPIO.py toggles a GPIO port as fast as it can. It is the fastest speed yes and goes faster with no usleep.

## i2c via the Kernel Driver
i2cKernel.sh runs a shell script that displays the temperature in milli-degrees Celsius.

## Control the LED matrix from a browser
Using browserEtch.py my code creates a browser that has 5 buttons. Up, down, left, right, and shake. The directions move the cursor the ways you would expect and the shake button clears the etch-a-sketch like a real etch-a-sketch works.