import cv2
import matplotlib.pyplot as plt
import numpy as np

#################   RASM o'qish  ############################
img = cv2.imread("Resources/news_i1.jpeg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("Output", img)
cv2.waitKey(0)

plt.figure()
plt.imshow(img_rgb)
# plt.imshow(img)
plt.show()


################## Video o'qish   ##########################
# video = cv2.VideoCapture("Resources/cr7.mp4")

# while True:
#     success, img = video.read()
#     print(img)
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break





#########################    READ WEBCAM  ###########################
# frameWidth = 640
# frameHeight = 480
# video = cv2.VideoCapture(0)
# video.set(3,frameWidth)
# video.set(4,frameHeight)
# video.set(10,130)
#
# while True:
#     success, img = video.read()
#     print(img)
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
