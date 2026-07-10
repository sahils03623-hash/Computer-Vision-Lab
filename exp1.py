import cv2

# Read the image
img = cv2.imread("image.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite("grayscale_output.png", gray)

# Show original image
cv2.imshow("Original Image", img)

# Show grayscale image
cv2.imshow("Grayscale Image", gray)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
