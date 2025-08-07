import cv2  # Import the OpenCV library for image processing

# Load the image from the specified file path
img = cv2.imread(r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\download.jpg")

# Apply Gaussian blur to the image
# (0, 0) means the kernel size is computed from the sigma value (here sigma=5)
# This blurs the image softly, reducing high-frequency details
blur = cv2.GaussianBlur(img, (0, 0), 5)

# Perform unsharp masking by combining the original and blurred image
# Formula: sharp = original * 1.5 + blurred * (-0.5) + 0
# This enhances edges by subtracting a portion of the blur from the original
sharpe = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

# Show the original image
cv2.imshow("Real Image", img)

# Show the blurred version of the image
cv2.imshow("Blur image", blur)

# Show the sharpened result after applying unsharp masking
cv2.imshow("Sharpe Image", sharpe)

# Wait for a key press indefinitely
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
