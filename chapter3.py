import cv2
import numpy as np


img = cv2.imread("Resources/news_i1.jpeg")
print(img.shape)
print(img)

imgResize = cv2.resize(img,(400, 300))

imgCropped = img[0:300, 300:600]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)