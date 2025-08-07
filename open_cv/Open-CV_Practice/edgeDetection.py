import cv2

img = cv2.imread('download (1).jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

edge = cv2.Canny(gray, 100,200)

cv2.imshow("Edge of image",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()