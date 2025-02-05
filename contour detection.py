import cv2 as cv
import numpy as np
 
img = cv.imread ('/Users/reem/Desktop/Opencv/Photos/cats.jpg')
cv.imshow ('Kittens', img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow ('Blank', blank)

# NEXT STEP IS CONVERTING THE IMAGE TO GREY
grey = cv.cvtColor (img , cv.COLOR_RGB2GRAY)
cv.imshow ('grey', grey)

# WE BLURRED TO GET BETTER EDGES
blur = cv.GaussianBlur (grey , (5,5), cv.BORDER_DEFAULT)

# THEN DETECT EDGES USING CANNY
canny = cv.Canny (blur , 125,175)
cv.imshow('canny edges', canny)


# INSTEAD OF BLURRING THEN CANNYING WE CAN USE THRESHOLD INSTEAD 
# ret , thresh = cv.threshold (grey , 125,255 , cv.THRESH_BINARY)
# cv.imshow('threshold img',thresh )


#THEN WE FIND THE COUNTOURS AND HIERARACHIES
contours, hierarachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #CHAIN_APPROX_NONE approximation method 
print (f'{len(contours)} contour(s) found!')

cv.drawContours (blank, contours, -1 , (0,0,255), thickness=1) # -1 means all countours
cv.imshow('countours', blank)




cv.waitKey(0)


