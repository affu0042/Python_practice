import cv2  # Import the OpenCV library for image processing
import numpy as np  # Import NumPy for handling arrays and matrices

# Load the image from the specified file path
img = cv2.imread(r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\download.jpg")

# Define a sharpening kernel (a 3x3 matrix)
# This kernel enhances the edges and details of the image
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Apply the sharpening filter to the image using the kernel
# cv2.filter2D applies a custom kernel to the image
# The '-1' means the output image has the same depth as the input image
sharpened = cv2.filter2D(img, -1, kernel)

# Display the original image in a window titled "Original image"
cv2.imshow("Original image", img)

# Display the sharpened image in a window titled "Sharpened image"
cv2.imshow('Sharpened image', sharpened)

# Wait for a key press indefinitely (0 milliseconds)
cv2.waitKey(0)

# Close all OpenCV windows after a key is pressed
cv2.destroyAllWindows()
