import cv2

# 1. Read an image
image = cv2.imread(r"C:\Users\OMO-MON-047\Desktop\Open-CV_Practice\istockphoto-1268291803-612x612.webp")

# 2. Show the image in a window
cv2.imshow("My Image", image)

# 3. Wait until any key is pressed
cv2.waitKey(0)

# 4. Save the image to disk
cv2.imwrite("output.jpg", image)

# 5. Close all windows
cv2.destroyAllWindows()
