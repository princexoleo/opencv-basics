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
        font = cv2.FONT_HERSHEY_SIMPLEX;
        text = "Some text on live video "
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA);
        cv2.imshow('Frame ', frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()