import cv2 as cv
import numpy as np

# there is 2 ways to draw on images : 1- draw on stand alone image 2- write on a dummy image or blank image to wrok with

blank = np.zeros ((500 , 500,3) , dtype = 'uint8') #uint8 is a data type of an image
cv.imshow ('blank', blank)


# 1. Paint the image a certain color 

# blank = np.zeros ((500 , 500 ,3) , dtype = 'uint8') # we added 3 because we need to give it a channel of three (the colors channels)
# blank[:] = 0,255,0  #[:] selecting all the pixeles 
# cv.imshow ('Green', blank)

# blank[:] = 0,0,255  #[:] selecting all the pixeles 
# cv.imshow ('red', blank)

# #painting a certain portion of the image by sending a range of pixeles
# blank [200:300 , 300:400] = 255 ,0 ,0
# cv.imshow ('certain propotion', blank)

#2. draw a rectangle

# cv.rectangle (blank, (0,0), (250,250), (0,255,0) , thickness=2) # (img , pt1 , pt2, color [,thikness [,linetype[,shift]]]) it takes these parameters
# cv.imshow ('rectangle', blank)

# # to fill whats inside the borders
# cv.rectangle (blank, (0,0), (250,250), (0,255,0) , thickness=cv.FILLED) #cv.filled or -1
# cv.imshow ('rectangle', blank)

# #3. draw a circle 
# cv.circle (blank , (100,250), 40 , (0,0,255) , thickness=-1) # the attributes it takes (img , center, radius "px" ,color, thickness, linetype)
# cv.imshow ('circle', blank)

# #4. draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,2550), thickness=3)
# cv.imshow ('line' , blank)

#writing text on an image

cv.putText (blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX , 1.0 , (255,0,0,), 2) 
cv.imshow ('text' , blank)

cv.waitKey(0)



