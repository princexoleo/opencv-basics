import  cv2
import  numpy as np

#img = cv2.imread('test.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8) # this will draw a black color image

# To draw a line on that image we have to call
# cv2.line(imageName, StartPoint(x,y), EndPoint(x,y),Color(B,G,R), Thickness)

img = cv2.line(img, (255,100), (300,200), (0, 0, 255), 10)
img = cv2.line(img, (255,100), (200,200), (0, 0, 255), 10)
img = cv2.line(img, (200,200), (300,200), (0, 0, 255), 10)
img = cv2.arrowedLine(img, (0,200), (155,200), (255, 0, 0), 10)  # Arrowed Line
# Draw rectangle
# cv2.rectangle(img , TopLeftVertex(x,y),LowerRightVertex(x2,y2),color(BGR),Thickness)
# x1,y1 ---------
# |              |
# |              |
# |              |
# |            x2,y2

img = cv2.rectangle(img, (10, 10), (100, 100), (0, 255, 0), 5)
# For circle cv2.circle(img, (center xy), radius, (color), thickness)
img = cv2.circle(img, (200,400), 50, (255, 0, 0), -1)
# Text
# cv2.putText(img, "Text", (startPoint),(fontFaces), fontSize, (fontColor),thickness, LineType)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv Text', (0,300), font, 2, (255,255,255), 5, cv2.LINE_AA)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
