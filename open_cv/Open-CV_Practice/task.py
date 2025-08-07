import cv2
import numpy as np

def apply_background_filter(input_path, output_path, filter_type="blur", intensity=10, color=(0, 255, 0)):
    """
    Apply a background filter to an image.
    filter_type options: "blur", "color", "virtual_bg"
    """

    # 1. Load the input image
    img = cv2.imread(input_path)
    if img is None:
        print("Error: Could not load image")
        return

    # 2. Convert image to grayscale for simple background separation
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Create a binary mask (rough segmentation)
    # Pixels brighter than 200 = background (0)
    # Pixels darker than 200 = foreground (255)
    _, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # 4. Blur the mask edges so the transition is smooth
    mask = cv2.GaussianBlur(mask, (15, 15), 0)

    # 5. Extract only the foreground (subject) using the mask
    foreground = cv2.bitwise_and(img, img, mask=mask)

    # 6. Prepare the background according to filter_type
    if filter_type == "blur":
        # Apply a strong blur to the original image for background
        background = cv2.GaussianBlur(img, (intensity * 10 + 1, intensity * 10 + 1), 0)
    elif filter_type == "color":
        # Create a solid color background (same size as original image)
        background = np.full_like(img, color)
    elif filter_type == "virtual_bg":
        # Use another image as background (replace "virtual_bg.jpg" with your file)
        virtual_bg = cv2.imread("virtual_bg.jpg")
        virtual_bg = cv2.resize(virtual_bg, (img.shape[1], img.shape[0]))
        background = virtual_bg
    else:
        print("Invalid filter type. Using blur as default.")
        background = cv2.GaussianBlur(img, (51, 51), 0)

    # 7. Remove the foreground region from the background using the inverse mask
    background = cv2.bitwise_and(background, background, mask=255 - mask)

    # 8. Combine foreground and filtered background
    filtered_img = cv2.add(foreground, background)

    # 9. Save the final output image
    cv2.imwrite(output_path, filtered_img)

    # 10. Show the images for comparison
    cv2.imshow("Original", img)
    cv2.imshow("Filtered", filtered_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ==== MAIN EXECUTION ====
input_image = r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\download (1).jpg"      # Replace with your input file path
output_image = "filtered.jpg"   # Output file
apply_background_filter(input_image, output_image, filter_type="blur", intensity=5)
