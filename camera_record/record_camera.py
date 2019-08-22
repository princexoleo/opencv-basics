import cv2

cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # another option
# 1st parameter=name of output
# 2nd parameter = fourcc code
# 3rd parameter = frame rare
# 4th parameter = size (width and height)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))



if not cap.isOpened():
    print('camera open fialed!')


while True:
    ret, frame = cap.read()

    # chech ret calue
    if ret == True:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # GrayFrame

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        # to show the image
        cv2.imshow('frame', frame)
        cv2.imshow('GrayFrame', grayFrame)  # Another frame with color gray
        # press q to exit window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break




cap.release()
out.release()
cv2.destroyAllWindows()

