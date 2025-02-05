import cv2 as cv

#Rescaling

def rescaleFrame (frame , scale =0.75):
    width = int(frame.shape[1] * scale)  #1 is the width
    height= int(frame.shape[0] * scale)  # 0 is the height
    dimentions = (width , height)

    return cv.resize (frame , dimentions, interpolation =cv.INTER_AREA)

#Reading video 
capture = cv.VideoCapture ('/Users/reem/Desktop/Opencv/Videos/dog.mp4') # it take an integer value or path, integer if you are using camera (web cam =0)

while True :
    isTrue, frame = capture.read()      #it reads the video frame by frame

    #frame_resized= rescaleFrame(frame)
    frame_resized= rescaleFrame(frame , 0.20)  #the new resized frame using our rescaleFrame function
    cv.imshow ('Dog video' , frame)     # displays every frame of the video
    cv.imshow('video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): # if the letter d is pressed break out of this loop
        break

capture.release()
cv.destroyAllWindows()



#RESIZED IMAGE

img = cv.imread ('/Users/reem/Desktop/Opencv/Photos/cat_large.jpg')
resized_img= rescaleFrame(img)
cv.imshow ('cat' , img)
cv.imshow ('cat' , resized_img)



