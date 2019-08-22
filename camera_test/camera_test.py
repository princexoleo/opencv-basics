
import cv2

# print(cv2.__version__) # this is will print the version of opnev

cap = cv2.VideoCapture(0)  # this is will capture image from webcam/camera

# Check camera open correct or not
if not cap.isOpened():
    print('camera open fialed!')

# to capture continuous image we need infinite loop
while True:
    ret , frame = cap.read()
    
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # GrayFrame

    # to show the image
    cv2.imshow('frame', frame)
    cv2.imshow('GrayFrame', grayFrame)  # Another frame with color gray
    # press q to exit window
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break