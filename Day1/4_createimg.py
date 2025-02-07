import cv2
import numpy as np

img1 = np.zeros((240,320), dtype=np.uint8)
img2 = np.empty((240,320), dtype=np.uint8)
img3 = np.ones((240,320), dtype=np.uint8) * 150 #1로 채워져 있는것에 150을 곱한것 -> 모든 픽셀정보가 150
img4 = np.full((240,320,3), (255,102,255), dtype=np.uint8)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
cv2.waitKey()