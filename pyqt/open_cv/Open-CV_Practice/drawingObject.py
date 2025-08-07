import cv2  # Import OpenCV library

# 1️⃣ Draw a Circle
# Load the image from disk
Img_Circle = cv2.imread(r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\Physical (63).jpg")
if Img_Circle is not None:
    circle_img = Img_Circle.copy()  # Copy to preserve original
    # Draw a filled circle at position (100, 100) with radius 75 and color (B=0, G=127, R=127)
    cv2.circle(circle_img, (100, 100), 75, (0, 127, 127), -1)
    cv2.imshow("Circle", circle_img)
else:
    print("Circle image not found!")
# 2️⃣ Draw a Line
# Load another image
Img_Line = cv2.imread(r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\images (1).jpg")
if Img_Line is not None:
    line_img = Img_Line.copy()
    # Draw a red line from top-left (0,0) to (250,250) with thickness 2
    cv2.line(line_img, (0, 0), (250, 250), (0, 0, 255), 2)
    cv2.imshow("Line", line_img)
else:
    print("Line image not found!")

# 3️⃣ Draw a Rectangle
# Load another image
Img_Rectangle = cv2.imread(r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\istockphoto-1268291803-612x612.webp")
if Img_Rectangle is not None:
    rect_img = Img_Rectangle.copy()
    # Draw a black rectangle from point (20,20) to (150,150) with thickness 2
    cv2.rectangle(rect_img, (20, 20), (150, 150), (0, 0, 0), 2)
    cv2.imshow("Rectangle", rect_img)
else:
    print("Rectangle image not found!")

# 4️⃣ Add Text
# Load another image
Img_Text = cv2.imread(r"C:\Users\OMOLP76\Desktop\python\open_cv\Open-CV_Practice\abc.jpg")
if Img_Text is not None:
    text_img = Img_Text.copy()
    # Add red text "Open CV Practice" at position (150,150), using duplex font, scale 2, thickness 2
    cv2.putText(text_img, "Open CV Practice", (150, 150), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
    cv2.imshow("Text", text_img)
else:
    print("Text image not found!")
# 🕐 Wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
