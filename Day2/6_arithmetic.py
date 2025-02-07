# add, addWeighted, subtract, absdiff
# matplotlib의 subplot를 이용하여 4가지 연산결과를 출력
# absdiff(img1,img2)

import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('./dog.jpg')
img2 = cv2.imread('./square.bmp')

alpha = 0.7
dst1 = cv2.add(img1, img2)
dst2 = cv2.addWeighted(img1, 0.5 , img2, 0.5, 0)
dst3 = cv2.subtract(img1, img2)
dst4 = cv2.absdiff(img1, img2)

img = {'dst1': dst1, 'dst2': dst2, 'dst3': dst3, 'dst4': dst4}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i + 1)
    plt.imshow(v[:, : ,::-1]) # 행, 열, 채널 ( 채널의 순서를 역순으로 바꿔줌 -> -1 ) BGR -> RGB
    plt.title(k)
plt.show()



