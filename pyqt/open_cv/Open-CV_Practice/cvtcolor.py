import cv2
import matplotlib.pyplot as plt

img = cv2.imread("istockphoto-1268291803-612x612.webp")

grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

blue_channel, green_channel, red_channel = cv2.split(img)

plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
plt.imshow(img)
plt.title("Original image")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(grayscale, cmap="gray")
plt.title("grayscale image")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(rgb)
plt.title("RGB Color image")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(red_channel, cmap="Reds")
plt.title("Red color ")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(green_channel, cmap="Greens")
plt.title("green color ")
plt.axis("off")

plt.subplot(2,3,6)
plt.imshow(blue_channel, cmap="Blues")
plt.title("blue color ")
plt.axis("off")

plt.tight_layout()
plt.show()

