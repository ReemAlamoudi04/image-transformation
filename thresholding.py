# Thresholding is binarizing of an image, where the image pixeles are either 0 (black), or 255 (white)
# 2 types of thresholding : simple, adaptive
import cv2 as cv

img = cv.imread ('/Users/reem/Desktop/Opencv/Photos/cats.jpg')
cv.imshow ('cat' , img)

#Simple thresholding
# 1. converting the image into greyscale 
grey=cv.cvtColor (img, cv.COLOR_BGR2GRAY)
cv.imshow ('cat in grey', grey)

# 2. we use the thresholding function that returns threshold, thres, we pass the grey mage and the values(it basically says if its greater that 150 then set it to white)
threshold, thresh= cv.threshold(grey , 150 , 255, cv.THRESH_BINARY)   #150 is the thresholdded value , 255 is the maximum value
cv.imshow('simple thresholded', thresh)

#we can create an inversed thresholded image

threshold, thresh_inverse= cv.threshold(grey , 150 , 255, cv.THRESH_BINARY_INV)
cv.imshow('simple inverse thresholded', thresh_inverse)

#adaptive thresholding (we dont have to manually set the values of threshold, instead we let the computer find the optimal values)
adp_threshold = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) # 11 is the kernel size (window), we can use gaussian method not only mean
cv.imshow ('adaptive thresholding', adp_threshold)

adp_threshold2 = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 7) # 11 is he block size
cv.imshow ('adaptive thresholding2', adp_threshold2)

cv.waitKey(0)