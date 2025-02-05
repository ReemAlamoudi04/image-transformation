#computing edges in an image
import cv2 as cv 
import numpy as np
img = cv.imread ('/Users/reem/Desktop/Opencv/Photos/park.jpg')
cv.imshow ('cat' , img)

#firstly we need to convert the image to greyscale
grey= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow ('cat in grey', grey)

#1. Laplacion method 
lap= cv.Laplacian(grey, cv.CV_64F) #cv.64f is data depth
lap = np.uint8 (np.absolute(lap))
cv.imshow ('Laplacion method ', lap)

#2. sobel --> it computes gradient in 2 directions (x,y)
sobelx= cv.Sobel(grey, cv.CV_64F, 1 , 0) #1 hs x , 0 is y 
sobely= cv.Sobel(grey, cv.CV_64F, 0 , 1) #1 hs x , 0 is y 
cv.imshow ('sobel x' , sobelx)
cv.imshow ('sobel y' , sobely)
#combined sobel image 

combined_sobel = cv.bitwise_or(sobelx ,sobely)
cv.imshow ('combined_sobel' , combined_sobel)


# def combined_sobel (sobelx ,sobely):
#     sobelx= cv.Sobel(grey, cv.CV_64F, 1 , 0) #1 hs x , 0 is y 
#     sobely= cv.Sobel(grey, cv.CV_64F, 0 , 1) #1 hs x , 0 is y 






cv.waitKey(0)