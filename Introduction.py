import cv2

img = cv2.imread("mouse-soldier.png", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(img[0,0])

cv2.imshow("Mouse Man", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

grey_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY, )
cv2.imwrite("grey-mouse.jpg", grey_image)