import cv2

img = cv2.imread('./candies.png')
print('shape: ', img.shape)
print('dtype: ', img.dtype)

# b, g, r = cv2.split(img)

# 인덱스를 이용하는 방법
b = img[:, :, 0]  # Blue channel
g = img[:, :, 1]  # Green channel
r = img[:, :, 2]  # Red channel

cv2.imshow('img', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey()
