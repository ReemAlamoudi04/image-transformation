import cv2 as cv

img = cv.imread('/Users/reem/Desktop/Opencv/Photos/lady.jpg')
cv.imshow ('Lady' , img)


#1. converting rgb image to greyscale

gray = cv.cvtColor (img , cv.COLOR_RGB2GRAY)
cv.imshow ('Lady in grey' , gray)


#2. blur an image (can be used to remove noise)
blur = cv.GaussianBlur(img , (7,7), cv.BORDER_DEFAULT) # this is the blurring scale (7,7)
cv.imshow ('blur' , blur)


#3. Edge cascade
canny = cv.Canny (img , 125,175)
cv.imshow ('canny', canny)


canny = cv.Canny (blur , 125,175) # we  can reducce the lines ofthe image by passing the blurred image instead of og image
cv.imshow ('canny', canny)


#4. dialating the image
dilated = cv.dilate(canny , (7,7), iterations=3)
cv.imshow ('dilated', dilated)


#5. eroding
eroded = cv.erode(dilated , (3,3), iterations=3)
cv.imshow ('eroded', eroded)

#6. resize
resized = cv.resize(img , (500, 500), interpolation=cv.INTER_AREA)  #if you wanna shring an image use interpolation=cv.INTER_AREA                                                    
                                                                     #if you wanna shring an image use interpolation=cv.INTER_CUBIC 
cv.imshow('resized', resized)   #resized the image ignoring the aspect ration

#7. Cropping 
cropped = img [50:200 , 200:400]
cv.namedWindow("crop")
cv.imshow('cropped', cropped)














cv.waitKey (0)


