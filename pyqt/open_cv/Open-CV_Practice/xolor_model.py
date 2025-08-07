import cv2
import matplotlib.pyplot as plt
# Load the image in color
image = cv2.imread('xample.jpg') # Replace with your image path
# Convert BGR (OpenCV default) to RGB for Matplotlib display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Split the channels (Note: OpenCV uses BGR, so order is Blue, Green, Red)
blue_channel, green_channel, red_channel = cv2.split(image)
# Plotting the results
plt.figure(figsize=(12, 8))
# Original RGB Image
plt.subplot(2, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Image (RGB)')
plt.axis('off')
# Grayscale Image
plt.subplot(2, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
# Red Channel
plt.subplot(2, 3, 4)
plt.imshow(red_channel, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')
# Green Channel
plt.subplot(2, 3, 5)
plt.imshow(green_channel, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')
# Blue Channel
plt.subplot(2, 3, 6)
plt.imshow(blue_channel, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')
plt.tight_layout()
plt.show()
