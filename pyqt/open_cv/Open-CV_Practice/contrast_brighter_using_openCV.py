import cv2
# Function to apply brightness and contrast
def update(val):
    brightness = cv2.getTrackbarPos('Brightness', 'Image Adjuster') - 100
    contrast = cv2.getTrackbarPos('Contrast', 'Image Adjuster') - 100
    adjusted = cv2.convertScaleAbs(img, alpha=1 + contrast / 100.0, beta=brightness)
    cv2.imshow('Image Adjuster', adjusted)
# Load the image
img = cv2.imread('istockphoto-1268291803-612x612.webp') # Replace with your image path
# Create a window
cv2.namedWindow('Image Adjuster')
# Create trackbars for brightness and contrast
cv2.createTrackbar('Brightness', 'Image Adjuster', 100, 200, update)
cv2.createTrackbar('Contrast', 'Image Adjuster', 100, 200, update)
# Initialize with original image
update(0)
# Wait until user presses a key
cv2.waitKey(0)
cv2.destroyAllWindows()
