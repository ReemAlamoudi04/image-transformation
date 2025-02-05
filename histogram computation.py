#histograms allow us to visualizr the distribution of pixels internsity 

import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread ('/Users/reem/Desktop/Opencv/Photos/cats.jpg')
cv.imshow('cats', img)

grey= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow ('grey', grey)

#grayscale histogram

gray_hist = cv.calcHist ([grey] , [0], None ,[256], [0,256] )

plt.figure()
plt.title('grey scale histogram')
plt.xlabel('bins')
plt.ylabel('# of pixles')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)