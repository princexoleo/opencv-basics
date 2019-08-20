import numpy as np
import cv2

cap = cv2.VideoCapture(0)  #this is will capture image from webcam/camera

#to capture continuous image we need infinite loop
while True:
    ret , frame = cap.read()

    #to show the image
    cv2.imshow('frame', frame)