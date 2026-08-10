import cv2

img = cv2.imread("Rotate.png")

rotated_clockwise = cv2.rotate(
    img, cv2.ROTATE_90_CLOCKWISE
)

rotated_counterclockwise = cv2.rotate(
    img, cv2.ROTATE_90_COUNTERCLOCKWISE
)

cv2.imwrite("Rotate_Clockwise.png", rotated_clockwise)
cv2.imwrite("Rotate_CounterClockwise.png", rotated_counterclockwise)

cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", rotated_clockwise)
cv2.imshow("Counter Clockwise Rotation", rotated_counterclockwise)

cv2.waitKey(0)
cv2.destroyAllWindows()