import cv2 as cv #importing opencv

#READING IMAGES
img = cv.imread('/Users/reem/Desktop/Opencv/Photos/cat_large.jpg') # read an image
cv.imshow('Cat' , img) #display the image as a new window

cv.waitKey (0)




#READING VIDEOS
capture = cv.VideoCapture ('rtsp://admin:prime147@192.168.11.190:554/Streaming/Channels/101/') # it take an integer value or path, integer if you are using camera (web cam =0)

while True :
    isTrue, frame = capture.read()      #it reads the video frame by frame
    cv.imshow ('Dog video' , frame)     # displays every frame of the video

    if cv.waitKey(20) & 0xFF==ord('d'): # if the letter d is pressed break out of this loop
        break

capture.release()
cv.destroyAllWindows()




