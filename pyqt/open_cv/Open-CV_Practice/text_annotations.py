import cv2  # Import OpenCV library for image processing
import numpy as np  # Import NumPy for numerical operations

# Create a blank white image of size 400x600 with 3 color channels (BGR)
img = np.ones((400, 600, 3), dtype=np.uint8) * 255

# List of text annotations with different fonts
annotaions = [
    {
        "text": "Small Text",  # The text string
        "pos": (0, 100),  # Position where text will be placed
        "font": cv2.FONT_HERSHEY_COMPLEX,  # Font style: complex
        "scale": 1.5,  # Font size
        "color": (0, 0, 0),  # Font color: black
        "thickness": 1  # Thickness of text
    },
    {
        "text": "Small Text",
        "pos": (0, 200),
        "font": cv2.FONT_HERSHEY_COMPLEX_SMALL,  # Font style: complex small
        "scale": 1.5,
        "color": (0, 0, 0),
        "thickness": 1
    },
    {
        "text": "Plain Text",
        "pos": (0, 300),
        "font": cv2.FONT_HERSHEY_PLAIN,  # Font style: plain
        "scale": 1.5,
        "color": (0, 0, 0),
        "thickness": 1
    }
]

# Loop through each annotation and draw the text on the image
for annotation in annotaions:
    cv2.putText(
        img,  # Image on which to draw
        annotation['text'],  # Text to draw
        annotation['pos'],  # Position of text
        annotation['font'],  # Font type
        annotation['scale'],  # Font scale
        annotation['color'],  # Font color
        annotation['thickness']  # Thickness of the font
    )

# Display the final image with all text annotations
cv2.imshow("Labelled Image", img)
cv2.waitKey(0)  # Wait for any key to be pressed
cv2.destroyAllWindows()  # Close all OpenCV windows
