import cv2
import matplotlib as plt

img= cv2.imread("/Users/reem/Desktop/Opencv/Photos/cat_large.jpg")
cv2.imshow('cat', img)

grey_img= cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
cv2.imshow('grey cat', grey_img)

contoured, hierarchy= cv2.findContours(grey_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for index in range (len(contoured)):
    c= contoured[index]
    x1,y1,x2,y2= cv2.boundingRect(c)
    cv2.rectangle (grey_img, (0,0), (250,250), (0,255,0) , thickness=2)


cv2.imshow(grey_img)

cv2.waitKey(0)
cv2.destroyAllWindows() 