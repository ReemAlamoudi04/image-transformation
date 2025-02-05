import cv2 as cv 
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow ('Boston' , img)

#1. Translation (shifting an image along x and y axis) up,dowm,left , right
# -x --> left
#  x --> Right
# -y --> up
#  y --> down


def translate (img , x , y):  # (img , x , y)
    transMat = np.float32 ([[1,0,x],[0,1,y]])    #to translate an image we need to create a translation matrix 
    dimentions= (img.shape[1], img.shape[0])     # 1 is the widht 0 is the height
    return cv.warpAffine (img , transMat, dimentions)

translated_img= translate (img , 100 ,100)
cv.imshow ('translated' ,translated_img)

translated_img2= translate (img , -100 ,-200)
cv.imshow ('translated2' ,translated_img2)

#2. Roation

def rotate (img , angle , rotPoint = None):
    (height,width)= img.shape [:2]

    if rotPoint is None:
        rotPoint = (width//2 , height//2)    # rotating around the center

    rotMat= cv.getRotationMatrix2D(rotPoint, angle,1.0)
    dimentios = (width,height)
    return cv.warpAffine (img , rotMat , dimentios)

rotated_img = rotate (img, 45)
cv.imshow ('rotated_img' , rotated_img)


#3. Resize image 

resized = cv.resize(img , (500,500) , interpolation=cv.INTER_AREA)
cv.imshow('resize', resized)


#4. flipping

flip = cv.flip (img, -1 ) # 0--> vertacaly 1--> horazontally 2-> both
cv.imshow ('flip', flip )


#5. Cropping 
cropped = img [50:200 , 200:400]
cv.imshow('cropped', cropped)





















cv.waitKey(0)
