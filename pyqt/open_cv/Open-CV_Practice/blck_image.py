import numpy as np
import cv2 

img = np.zeros((512,512,3), dtype=np.uint8)

cv2.imshow("current window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

