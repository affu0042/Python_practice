# Import necessary libraries
import cv2
import numpy as np
from google.colab.patches import cv2_imshow  # Special function to display images in Google Colab

# Step 1: Load the image
image = cv2.imread("/content/cat.png")  # Replace with your image path
# cv2.imread reads the image from disk and stores it as a NumPy array.
# If the path is wrong, it returns None.

# Step 2: Rotate the image by 90 degrees clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
# cv2.rotate applies predefined rotation (90° clockwise in this case).

# Step 3: Flip the image
flipped_h = cv2.flip(image, 1)  # Horizontal flip (mirror along vertical axis)
flipped_v = cv2.flip(image, 0)  # Vertical flip (mirror along horizontal axis)
# cv2.flip(image, flipCode)
# flipCode = 1 -> Horizontal flip
# flipCode = 0 -> Vertical flip
# flipCode = -1 -> Both

# Step 4: Affine transformation (shearing)
rows, cols, _ = image.shape  # Get image dimensions (height, width, channels)

# Define three points in the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# Define where those points should move to
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
# This mapping will cause a shearing effect.

# Get the 2x3 affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply the affine transformation
transformed = cv2.warpAffine(image, matrix, (cols, rows))
# cv2.warpAffine applies the transformation matrix to the image and outputs a new image.

# Step 5: Display all images
cv2_imshow(image)        # Original image
cv2_imshow(rotated)      # Rotated image
cv2_imshow(flipped_h)    # Horizontally flipped
cv2_imshow(flipped_v)    # Vertically flipped
cv2_imshow(transformed)  # Affine transformed image

# Note: cv2.waitKey() and cv2.destroyAllWindows() are used in normal Python scripts
# but are not necessary in Google Colab, so we skip them here.
