# hw01.py Operating Instrucitons
This file's purpose is to walk you through how to use hw01.py

## What it does
This file allows the user to play on an Etch-A-Sketch on their terminal. The user will be allowed to pick their own size of matrix and will be able to move their cursor in the up, down, left, and right directions. The rest of this document will walk you through how to use the file.

## How to start
cd into the correct directory then enter this line
```bash
$ python3 hw01.py
```

## Use
The first thing you will see is:
```python
Enter a Matrix Size:
```
The input 'a' will create an axa matrix that will be the Etch-A-Sketch size

Next you will be asked:
'''python
Use WASD to operate Etch-A-Sketch or spacebar to shake 
'''
Each button input does a different task:
W - moves cursor up if able
A - moves cursor left if able
S - moves cursor down if able
D - moves cursor right if able
Space Bar - clears the Etch-A-Sketch but keeps current position the same

An enter is required after each button press
To exit the Etch-A-Sketch simply press ctrl+C

After each button input, your new Sketch is printed and you can begin to draw your pictures!

# hw01 grading

| Points      | Description |
| ----------- | ----------- |
|  8 | Etch-a-Sketch works
|  2 | Code documented (Add your name)
|  2 | Includes #!/usr/bin/env python3 and chmod +x
|  2 | install.sh included if needed
|  2 | Used hw01 directory
|  2 | ReadMe.md included
|  2 | Name in gitLearn and gitLearnFork
| 20 | **Total**
