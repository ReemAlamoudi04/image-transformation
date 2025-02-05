# CHANGINF RESOLUTION WORKS FOR *LIVE VIDEO ONLY*

import cv2 as cv
#READING VIDEOS
capture = cv.VideoCapture ('/Users/reem/Desktop/Opencv/Videos/dog.mp4') # it take an integer value or path, integer if you are using camera (web cam =0)

while True :
    isTrue, frame = capture.read()      #it reads the video frame by frame
    cv.imshow ('Dog video' , frame)     # displays every frame of the video

    if cv.waitKey(20) & 0xFF==ord('d'): # if the letter d is pressed break out of this loop
        break

capture.release()
cv.destroyAllWindows()




def changeRes (width , height):
    capture.set (3, width)
    capture.set (4 , height)

