import cv2
import numpy as np
# import matplotlib.pyplot as plt



img = cv2.imread("Resources/news_i1.jpeg")
kernel = np.ones((5,5), np.uint8)
print(kernel)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)
imgCanny = cv2.Canny(img, 150, 200)

cv2. imshow("Gray Image", imgGray)
cv2. imshow("Blur Image", imgBlur)
cv2. imshow("Canny Image", imgCanny)
cv2. waitKey(0)