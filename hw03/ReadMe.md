# hw03
- TMP101
- Etch-a-sketch

This repository contains all of the files that are required for the hw03 submission. This assignment turned our etch-a-sketch into a playable game on an 8x8 LED matrix. 

## TMP101
The files temperatureRead.sh, temperatureRead.py, temperatureInterrupt.py, and interruptSetup.sh are all part of this section. My temperatureRead files take the inputs of the two temperature sensors, convert them to Farenheit, and then display the temperatures on the terminal. I unfortunately did not get to finish the temperature Interrupt. I could not figure out how to set up my alerts and because of that could not move forward with the section.

## Etch-a-sketch
The file for this is hw03.py

## What it does
This file allows the user to play on an Etch-A-Sketch on an 8x8 LED matrix. There are 4 buttons that control movement of the etch-a-sketch. The rest of this document will walk you through how to play.

## How to start
cd into the correct directory then enter this line
```bash
$ sudo python3 ./hw03.py
```
## Use
The game will automatically boot up and your cursor will begin as a yellow dot in the bottom right corner. 

At this point, you will now use the pushbuttons on the breadboard

The top button will control up movement.
The second button will control left movements.
The third button will control right movements.
The bottom button will control down movements.

After each button press, you will see your cursor move about the LED matrix. The cursor will be the color yellow and the places you have been will be green.

There are two features that implement the temperature sensors.

# Overheating mode
If the top temperature sensor reaches a temperature above 79.5 degrees F, the LED matrix enters 'Overheating mode'. In this mode, the LED will be all red and will need to be reset.

# Reset Button
If the bottom temperature sensor reaches a temperature above 79.5 degrees F, the LED matrix will reset. Similarly to if you shook a real Etch-a-Sketch. The current curson position will stay the same, but all your work will be erased.

# hw03 grading

| Points      | Description |
| ----------- | ----------- |
|  5/5 | TMP101 
|  3/3 |   | setup.sh
|  2/2 |   | Documentation 
|  5/5 | Etch-a-Sketch
|  3/3 |   | setup.sh
|  2/2 |   | Documentation
| 20/20 | **Total**

Very well done.  No problem not getting the overtemp interupt working.
