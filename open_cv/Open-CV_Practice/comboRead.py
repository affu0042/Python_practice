import cv2

img1 = cv2.imread('download (1).jpg',cv2.IMREAD_COLOR)
cv2.imshow("I am reading an color image",img1)
img2 = cv2.imread('download (1).jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("I'm reading a grayscale image",img2)
img3 = cv2.imread('download (1).jpg',cv2.IMREAD_UNCHANGED)
cv2.imshow("I am reading a unchanged image",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()

