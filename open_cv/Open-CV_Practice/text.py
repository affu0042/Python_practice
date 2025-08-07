import cv2  # Import OpenCV library for image processing

# Load the image from the specified path
pic = cv2.imread(r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\output.jpg")

# Check if the image was loaded correctly
if pic is None:
    print("No image is not found")  # If image loading fails, print this
else:
    Image = pic  # Assign the loaded image to a variable named 'Image'

    # Define text to overlay on the image
    text = "OMOTEC"  # The text string to put
    position = (50, 50)  # Coordinates (x, y) where the text starts
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # Font style
    font_scale = 1  # Size of the text
    color = (0, 0, 0)  # Text color in BGR format (black)
    thickness = 1  # Thickness of the text stroke

    # Add text to the image
    cv2.putText(Image, text, position, font, font_scale, color, thickness)

    # Display the image in a window
    cv2.imshow("Labelled Image", pic)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
