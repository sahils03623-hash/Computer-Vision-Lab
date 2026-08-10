import cv2

img = cv2.imread("Rotate.png")

cv2.imshow("Original Image", img)

cv2.moveWindow("Original Image", 300, 200)

cv2.waitKey(0)
cv2.destroyAllWindows()