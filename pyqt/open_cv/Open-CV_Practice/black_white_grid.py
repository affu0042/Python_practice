import numpy as np 
import cv2

def grid_(row=10, cols=10,size=20):
    grid =  np.ones((row*size, cols*size),dtype=np.uint8) * 255
    for i in range(row):
        for j in range(cols):
            if (i+j)%2 == 0:
                grid[i*size:(i+1)*size,j*size:(j+1)*size] = 0
    return grid
cv2.imshow('chess board grid',grid_())
cv2.waitKey(0)
cv2.destroyAllWindows()