# hw04
- Memory Map
- GPIO via mmap
- i2c via the Kernel Driver
- Control the LED matrix from a browser
- LCD Display

## Memory Map
I attached my memory map that I created as MemoryMap.png

## GPIO via mmap
buttonLED.py covers the first part. This code reads from two switches to control 2 LEDs
mmapGPIO.py is the file for the second part of this section. mmapGPIO.py toggles a GPIO port as fast as it can. It is the fastest speed yes and goes faster with no usleep.

*How fast does it go?*

## i2c via the Kernel Driver
i2cKernel.sh runs a shell script that displays the temperature in milli-degrees Celsius.

*cd's shouldn't be in loop.*

## Control the LED matrix from a browser
Using browserEtch.py my code creates a browser that has 5 buttons. Up, down, left, right, and shake. The directions move the cursor the ways you would expect and the shake button clears the etch-a-sketch like a real etch-a-sketch works.

## LCD Display
For my LCD display, I got to display Boris, Boris rotated 90 degrees, and Boris with text. I also played a RedsNightmare.mpg on the LCD display as well.


# hw04 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Memory map 
|  4/4 | mmap()
|  4/4 | i2c via Kernel
|  5/5 | Etch-a-Sketch via flask
|  5/5 | LCD display
|      | Extras
| 20/20 | **Total**

*My comments are in italics. --may*

