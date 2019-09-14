import cv2

# print(cv2.__version__) # this is will print the version of opnev

cap = cv2.VideoCapture(0)  # this is will capture image from webcam/camera

# Check camera open correct or not
if not cap.isOpened():
    print('camera open fialed!')

# to capture continuous image we need infinite loop
while True:
    ret, frame = cap.read()  # ret contains true/false and frame contains the image

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # GrayFrame

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # to show the image
    cv2.imshow('frame', frame)
    cv2.imshow('GrayFrame', grayFrame)  # Another frame with color gray
    # press q to exit window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
#  video capture properties
#  link: https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
