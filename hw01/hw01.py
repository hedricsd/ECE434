import numpy as np
import sys

def clearArray(rows, cols, curX, curY):
    array = np.empty([rows, cols], dtype = object)

    for a in range(rows):
        for b in range(cols):
            array[a, b] = '  '
    
    for a in range(size):
        array[0][a + 2] = str(a).zfill(2)
    for b in range(size):
        array[b + 1][0] = str(b).zfill(2)
        array[b + 1][1] = ':'
    array[curX, curY] = " X"
    return array
    
def printMatrix(a):
    rows = a.shape[0]
    cols = a.shape[1]
    for i in range(0,rows):
        for j in range(0,cols):
            print("%s" %a[i,j], end = ' ')
        print()


size = int(input("Enter a Matrix Size: "))
rows = size + 1
cols = size + 2
curX = 1
curY = 2

array = clearArray(rows, cols, curX, curY)


printMatrix(array)

while(1):
    movement = input("Use WASD to operate Etch-A-Sketch or spacebar to shake ")
    
    if(movement == "a"):
        if(curY > 2):
            curY-=1
    if(movement == "d"):
        if(curY < size + 1):
            curY+=1
    if(movement == "w"):
        if(curX > 1):
            curX-=1
    if(movement == "s"):
        if(curX < size):
            curX+=1
    if(movement == " "):
        array = clearArray(rows, cols, curX, curY)
        
    array[curX, curY] = " X"
    printMatrix(array)
    