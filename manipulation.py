import cv2
import numpy as np

img = cv2.imread("mouse-soldier.png", cv2.IMREAD_COLOR)


# RESIZE
img = cv2.resize(img, (400, 800))
img = cv2.resize(img, (0,0), fx=2, fy=1)
# CROP
height, width = img.shape[0], img.shape[1]

img = img[80 : int(height/2) -100 , 350 : -265]

# ROTATE
img = cv2.rotate(img, cv2.ROTATE_180)

# TRANSLATE



#cv2.imwrite("mouse-headshot.jpg", img)


#cv2.imshow("Mouse Guy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()