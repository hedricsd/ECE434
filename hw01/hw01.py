import numpy as np

# Function that clears/sets up the array while keeping the current X and current Y value the same
def clearArray(rows, cols, curX, curY):
    array = np.empty([rows, cols], dtype = object)

    for a in range(rows):
        for b in range(cols):
            array[a, b] = '  '
    
    for a in range(size):
        array[0][a + 2] = str(a).zfill(2) # zfill makes the array values all have 2 spaces so the format looks nicer
    for b in range(size):
        array[b + 1][0] = str(b).zfill(2)
        array[b + 1][1] = ':'
    array[curX, curY] = " X"
    return array
    
# Function that goes through the numpy array and prints it in an easier to understand format
def printMatrix(a):
    rows = a.shape[0]
    cols = a.shape[1]
    for i in range(0,rows):
        for j in range(0,cols):
            print("%s" %a[i,j], end = ' ') # end = ' ' makes it so it prints the array rows on one line
        print()

# Variable that I use to create array
size = int(input("Enter a Matrix Size: "))
rows = size + 1
cols = size + 2
curX = 1
curY = 2

# Initiallizing array
array = clearArray(rows, cols, curX, curY)

# Prints the first original matrix
printMatrix(array)

while(1):
    movement = input("Use WASD to operate Etch-A-Sketch or spacebar to shake ")
    
    # moves cursor in the left direction
    if(movement == "a"):
        if(curY > 2):
            curY-=1
            
    # moves cursor in the right direction
    if(movement == "d"):
        if(curY < size + 1):
            curY+=1
            
    # moves cursor in the up direction
    if(movement == "w"):
        if(curX > 1):
            curX-=1
            
    # moves cursor in the down direction
    if(movement == "s"):
        if(curX < size):
            curX+=1
            
    # Clears and resets the array
    if(movement == " "):
        array = clearArray(rows, cols, curX, curY)
        
    array[curX, curY] = " X" # prints an 'X' where the etch a sketch moves
    printMatrix(array) # reprints the new updated matrix
    