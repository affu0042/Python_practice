import cv2
import numpy as np

# Load the image in color
img = cv2.imread("abc.jpg")  # Read the image (BGR format)

# Convert the image to grayscale
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert BGR to Grayscale

# Set brightness and contrast parameters
alpha = 1.5  # Contrast factor (>1 increases contrast)
beta = 30    # Brightness value (>0 makes it brighter)

# Apply brightness and contrast adjustment
# Formula: new_pixel = alpha * original_pixel + beta
adjusted = np.clip(alpha * grayscale + beta, 0, 255).astype(np.uint8)  # Ensure values stay in [0,255]

# Display all three images in separate windows
cv2.imshow("Original Image", img)              # Original color image
cv2.imshow("Gray Image", grayscale)            # Grayscale image
cv2.imshow("Brighter and Sharper", adjusted)   # Adjusted grayscale image

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
