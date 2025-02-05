# we can split an image into its 3 color channels
import cv2 as cv
import numpy as np


img = cv.imread ('/Users/reem/Desktop/Opencv/Photos/park.jpg')
cv.imshow ('boston', img)
blank = np.zeros (img.shape[:2], dtype= 'uint8')


b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([g,blank,blank])
red = cv.merge([r,blank,blank])


cv.imshow('blue' , blue)
cv.imshow('green' ,green)
cv.imshow('red' ,  red)

#visualize the images 
print (img.shape)
print (b.shape)
print (g.shape)
print (r.shape)

#merge the color channels together 
merged = cv.merge([b,g,r])
cv.imshow('merged image' , merged)
cv.waitKey(0)
