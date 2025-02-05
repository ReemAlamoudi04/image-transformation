import cv2 as cv

img = cv.imread ('/Users/reem/Desktop/Opencv/Photos/park.jpg')
cv.imshow ('boston', img)


# BGR TO GRAY
grey = cv.cvtColor (img ,cv.COLOR_BGR2GRAY)
cv.imshow ('grey', grey)

#BGR TO HSV
hsv = cv.cvtColor (img, cv.COLOR_BGR2HSV)
cv.imshow ('hsv', hsv)

#BGR TO LAB
lab = cv.cvtColor (img, cv.COLOR_BGR2Lab)
cv.imshow ('lab', lab)

# !! we can also convert grayscale to gbr, hsv to gbr and so on
# but we can not directly change a greyscale into hsv we should first convert it back to gbr then to another formst





cv.waitKey(0)