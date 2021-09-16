# hw02 Grading specs
- Buttons and LEDS
- Measuring a gpio pin on an Oscilloscope
- GPIOD
- Security
- Etch-a-sketch

This repository contains all of the files that are required for the hw02 submission. This assignment builds off of the last one and implements a further design of my Etch-a-sketch. This time, instead of using WASD keys, I have push buttons to various GPIO pins that do the moving of the etch-a-sketch 'X'. The rest of this document will take you more through the individual steps.

## Buttons and LEDS
I wrote a python script called simpleButton.py to meet this requirement. My code takes 4 pushbuttons on the GPIO pins: 66, 67, 68, and 69. These 4 pushbuttons correlate to LEDs that are hooked up to GPIO pins: 30, 31, 50, and 60. When a push button is pressed, the corresponding LED turns on. When pushed again, the LED turns off.

## Measuring a gpio pin on an Oscilloscope
There were many parts to this part of my submission. They include:
- oscope.txt
- toggle.py
- toggle.sh
- toggle.c
- toggleResults.txt

### oscope.txt
This txt file contains all of the questions relating to the togglegpio.sh oscilloscope readings.

### toggle.pytoggle.sh/toggle.c
These files are the different ways that I attempted to toggle my gpio pin as fast as possible. Unfortunately, I was not able to get the C file to work correctly.

### toggleResults.txt
This txt file contains all of the results from my toggle files including a table of my findings with speed, frequency, and CPU usage of each type

## GPIOD
My results from this section can be found in the toggleResults.txt file as well

## Security
I set my bone to only be accessed on the port 1022. I then set up my fail2ban to have a 15 second lockout time when the ssh was failed 2 times.

## Etch-a-sketch
The file for this is hw02.py

## What it does
This file allows the user to play on an Etch-A-Sketch on their terminal. The user will be allowed to pick their own size of matrix and will be able to move their cursor in the up, down, left, and right directions. The rest of this document will walk you through how to use the file.

## How to start
cd into the correct directory then enter this line
```bash
$ ./hw01.py
```
## Use
The first thing you will see is:
```python
Enter a Matrix Size:
```
The input 'a' will create an axa matrix that will be the Etch-A-Sketch size

At this point, you will know use the pushbuttons on the breadboard

The top button will control up movement.
The second button will control left movements.
The third button will control right movements.
The bottom button will control down movements.

After each button press, your new Sketch is printed and you can begin to draw your pictures!