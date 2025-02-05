import cv2 as cv 
import os

capture= cv.VideoCapture(0)

if not capture.isOpened():
    print("unable to read camera feed")

output_dir = 'output image'         #store the imagess of out data set
os.makedirs(output_dir, exist_ok=True)

img_counter = 0

while True:
    ret, frame= capture.read()

    if not ret:
        break
    cv.imshow('Webcam', frame)
    k=cv.waitKey(1)

    if k%256==26:
        print ("escape hit, closing ....")
        break

    elif k%256 == ord ('c'):
        img_name =os.path.join(output_dir, "opencv_frame_{}.png".format(img_counter))
        cv.imwrite(img_name, frame)
        print("{}written!".format(img_name))
        img_counter+=1
    
capture.release()
cv.destroyAllWindows()





!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="iMqcUqZ7N1v6C3Zp8j9M")
project = rf.workspace("reem-alamoudi").project("vd-h9sop")
version = project.version(1)
dataset = version.download("coco")
