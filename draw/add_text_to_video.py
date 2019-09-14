import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# set properties
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)  # 3 for width
cap.set(4, 3000)  # 4 for height

print(cap.get(3), cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame ', gray)

        if cv2.waitKey(0) & 0xFF == ord('c'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()