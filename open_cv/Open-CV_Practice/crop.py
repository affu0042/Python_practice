import cv2  # Import OpenCV for image processing

# Function to crop an image into a square based on user-selected ROI
def crop_to_square(image_path, output_path):
    # Load the image from disk
    img = cv2.imread(image_path)

    # If image loading fails, stop the function
    if img is None:
        print("Error: Could not load image")
        return

    # Let the user manually select a rectangular region of interest (ROI)
    # A window will pop up where you can draw a rectangle; press ENTER or SPACE to confirm
    from_center = False  # False means ROI selection starts from the mouse drag corner
    r = cv2.selectROI("Select area (Press Enter to confirm)", img, from_center)

    # Close the ROI selection window after confirmation
    cv2.destroyAllWindows()

    # Extract ROI values: x,y = top-left corner, w = width, h = height
    x, y, w, h = r

    # Make the crop a square:
    # Choose the smaller dimension (width or height) so the square fits
    size = min(w, h)

    # Compute the center of the selected rectangle
    center_x = x + w // 2
    center_y = y + h // 2

    # Calculate square boundaries while ensuring we stay inside the image limits
    # img.shape gives (height, width, channels), so:
    # img.shape[1] = width, img.shape[0] = height
    x1 = max(0, center_x - size // 2)
    y1 = max(0, center_y - size // 2)
    x2 = min(img.shape[1], center_x + size // 2)
    y2 = min(img.shape[0], center_y + size // 2)

    # Perform the crop using array slicing (rows = y, cols = x)
    cropped = img[y1:y2, x1:x2]

    # Save the cropped image to disk
    cv2.imwrite(output_path, cropped)

    # Print a confirmation message
    print(f"Cropped image saved to {output_path}")

# --- Main Program ---
# Provide your file paths here
input_image = r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\download (1).jpg"         # Replace with your input image path
output_image = r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\c1.jpg"

# Call the function to execute cropping
crop_to_square(input_image, output_image)
