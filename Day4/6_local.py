import cv2
import numpy as np

img = cv2.imread('./rice.png', cv2.IMREAD_GRAYSCALE)

# 전역 자동 이진화
_, dst1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


# 지역 이동 이진화(4*4)
dst2 = np.zeros(img.shape, np.uint8)
bw = img.shape[1] // 4
bh = img.shape[0] // 4 # 크기를 똑같이 맞춰줄려고 하는것

for y in range(4):
    for x in range(4):
        img_ = img[y*bh: (y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst2[y*bh: (y+1)*bh, x*bw:(x+1)*bw]
        cv2.threshold(img_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_) # img 에서 이진화를 시킨것을 dst에 집어 넣는다

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
