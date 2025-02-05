import cv2 as cv


img = cv.imread ('/Users/reem/Desktop/Opencv/Photos/cats.jpg')
cv.imshow('cats', img)

#SMOOTHING AN IMAAG TO REDUCE SOME NOISE

#1. Averaging blur
average = cv.blur (img , (3,3))  # kernel size (3,3) the higher it is the blurrier it gets
cv.imshow ('Average blur', average )

#2. gaussian blur
gaus = cv.GaussianBlur(img, (3,3),0 ) # 0 is the standard deviation in  direction 
cv.imshow ('gaussian blur', gaus )

#3. median blurring --> similar to averaging, it is more effective for salt and pepper noise , not meant for high kernel sizes
median = cv.medianBlur(img ,3 )
cv.imshow('median blur', median)

#4. bilateral blurring --> the most effective
bilaterial = cv.bilateralFilter(img , 5, 15, 15)  #5 is a diameter not kernel, 15 sigma color , 15 sigma space 
cv.imshow('bilaterial blur', bilaterial)


cv.waitKey(0)