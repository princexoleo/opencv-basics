import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

#make_720p()
#change_res(1280, 720)

# change video resulation
#make_720p()
#change_res(800 , 800)
#make_480p()

# Rescale
def rescale_frame(frame, percent=75):
    scale_percent = percent 
    width         = int (frame.shape[1] * scale_percent/100)
    height        = int (frame.shape[0] * scale_percent/100)
    dim  = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)



# to capture continuous image we need infinite loop
while True:
    ret , frame = cap.read()
    frame = rescale_frame(frame,300)
    # to show the image
    cv2.imshow('frame', frame)
    # press q to exit window
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done , relase the capture
cv2.relase()
cv2.destroyAllWindows()