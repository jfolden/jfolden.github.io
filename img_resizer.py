import cv2

img = cv2.imread("img/prof4.png")
resized = cv2.resize(img, (300,150))
cv2.imshow('im',resized)
cv2.waitKey(0)