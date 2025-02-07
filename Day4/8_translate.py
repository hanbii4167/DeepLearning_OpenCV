import cv2
import numpy as np

img = cv2.imread('./dog.bmp')
aff = np.array([[1, 0, 200], [0, 1, 100]], dtype = np.float32)
dst = cv2.warpAffine(img, aff, (0,0))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()