import cv2

image = cv2.imread("images (1).jpg")

height, width = image.shape[:2]

scale_factor = 3.0
bigger_image = cv2.resize(image, (int(width * scale_factor), int(height * scale_factor)))

scale_factor = 0.5
smaller_image = cv2.resize(image, (int(width * scale_factor), int(height * scale_factor)))

cv2.imshow('Original Image', image)
cv2.imshow('Bigger Image', bigger_image)
cv2.imshow('Smaller Image', smaller_image)

cv2.imwrite("Bigger_image.jpg", bigger_image)
cv2.imwrite("Smaller_image.jpg", smaller_image)

cv2.waitKey(0)
cv2.destroyAllWindows()