import cv2

image = cv2.imread("image2.png")

blur = cv2.GaussianBlur(image, (5, 5), 10)

cv2.imwrite("blurred_output.png", blur)

cv2.imshow("Blurred Image", blur)

cv2.waitKey(0)

cv2.destroyAllWindows()