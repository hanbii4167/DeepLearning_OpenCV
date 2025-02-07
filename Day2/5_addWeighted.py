import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('./man.jpg')
img2 = cv2.imread('./turkey.jpg')


alpha = 0.7
dst1 = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0)
dst2 = img1 * alpha + img2 * (1-alpha)
dst2 = dst2.astype(np.uint8)


img = {'img1': img1, 'img2': img2, 'dst1': dst1, 'dst2': dst2}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i + 1)
    plt.imshow(v[:, : ,::-1]) # 행, 열, 채널 ( 채널의 순서를 역순으로 바꿔줌 -> -1 ) BGR -> RGB
    plt.title(k)
plt.show()
