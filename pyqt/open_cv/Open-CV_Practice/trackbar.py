import cv2
# Callback function that updates the image whenever a trackbar value changes
def update(val):
    # Get the current position of the Brightness trackbar (0 to 200), shift to -100 to +100
    brightness = cv2.getTrackbarPos('Brightness', 'Image Adjuster') - 100  
    # Get the current position of the Contrast trackbar (0 to 200), shift to -100 to +100
    contrast = cv2.getTrackbarPos('Contrast', 'Image Adjuster') - 100
    # Apply contrast and brightness adjustments using convertScaleAbs
    # alpha controls contrast (1.0 is no change), beta controls brightness
    adjusted = cv2.convertScaleAbs(img, alpha=1 + contrast / 100.0, beta=brightness)
    # Show the adjusted image in the same window
    cv2.imshow('Image Adjuster', adjusted)
# Load the image from file (make sure the image path is correct)
img = cv2.imread("images (1).jpg")
# Create a named window to display the image and attach trackbars
cv2.namedWindow('Image Adjuster')
# Create a trackbar for Brightness with initial value 100 (mapped to 0), max value 200
cv2.createTrackbar('Brightness', 'Image Adjuster', 100, 200, update)
# Create a trackbar for Contrast with initial value 100 (mapped to 0), max value 200
cv2.createTrackbar('Contrast', 'Image Adjuster', 100, 200, update)
# Call update() once at the start to show the image with default settings
update(0)
# Wait for any key press to exit
cv2.waitKey(0)
# Close all OpenCV windows
cv2.destroyAllWindows()
