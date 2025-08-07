import cv2  # Import the OpenCV library for image processing

# Read the image from file
img = cv2.imread('download (1).jpg')  
# This loads the image into a NumPy array (in BGR format)

# Apply Gaussian Blur to the image
bkurred = cv2.GaussianBlur(img, (15, 15), 0)  
# (15,15) is the size of the Gaussian kernel (must be odd numbers).
# 0 means the standard deviation (sigmaX) is computed automatically.
# This creates a soft, smooth blur effect.

# Show the blurred image in a window (Note: You should pass 'bkurred' instead of 'img')
cv2.imshow("Blur image", bkurred)  
# Opens a window titled "Blur image" and displays the blurred version

cv2.waitKey(0)  
# Waits indefinitely until any key is pressed

cv2.destroyAllWindows()  
# Closes all OpenCV image windows
