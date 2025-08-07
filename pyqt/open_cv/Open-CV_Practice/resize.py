import cv2

def resize(input, output, width=1024, height=900):
    # Read the image from the given file path
    img = cv2.imread(input)

    # If image not found, exit the function
    if img is None:
        print("No image found at given path.")
        return

    # img.shape[:2] returns (height, width)
    original_height, original_width = img.shape[:2]
    print(f"Original image size: {original_width} x {original_height}")

    # Resize the image to the specified width and height
    # (width, height) is passed as a tuple
    # INTER_AREA is good for downscaling (reducing size)
    resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    # Save the resized image to the output path
    cv2.imwrite(output, resized_img)

    print(f"Image resized to {width} x {height} and saved at: {output}")


# Input image path and output image path
input = r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\Physical (63).jpg"
output = r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\newresize.jpg"

# Call the function
resize(input, output)
