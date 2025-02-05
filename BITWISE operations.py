import cv2 as cv 
import numpy as np

blank = np.zeros((400,400), dtype = 'uint8')

rectangle= cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle (blank.copy(), (200,200), 200, 255, -1)
cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# bitwise AND --> returns the intersection of an image
biwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow ('bitwise and',biwise_and )

# bitwise or --> returns both intersection and non intersected reigions
biwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow ('bitwise or',biwise_or )

#bitwise xor --> reurn the non intersecting reigions
bitwise_xor = cv.bitwise_xor (rectangle,circle)
cv.imshow('bitwise xor', bitwise_xor)

#bitwise not --> returns nothing it just revert the binart columns
bitwise_not = cv.bitwise_not(rectangle) #it takes one parameter 
cv.imshow('not', bitwise_not)



cv.waitKey(0)
