# masking with bitwise operations --> allowing us to focus on a certain part of an image 
import cv2 as cv
import numpy as np 

img = cv.imread ('/Users/reem/Desktop/Opencv/Photos/cats.jpg')
cv.imshow('cats', img)

blank = np.zeros (img.shape[:2], dtype= 'uint8')

mask= cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) #img.shape[1]//2, img.shape[0]//2 +80
cv.imshow('mask',mask)

masked_img = cv.bitwise_and(img,img, mask=mask)
cv.imshow('masked_img',masked_img)









cv.waitKey(0)