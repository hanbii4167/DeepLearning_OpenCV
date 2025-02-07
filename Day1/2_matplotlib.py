import cv2
import matplotlib.pyplot as plt


'''
#cv2  통해서 그레이스케일로 불러온 후 matplotlib으로 그레이스케일영상 출력
img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('img', img)
#cv2.waitKey()

plt.axis('off')
plt.imshow(img, cmap='gray')
plt.show()
'''

'''
#cv2  통해서 컬러로 불러온 후 matplotlib으로 그레이스케일영상 출력
#openCV : BGR , matplotlib : RGB
img = cv2.imread('./dog.bmp')
plt.axis('off')
plt.imshow(img)
plt.show()
'''

'''
#cv2  통해서 컬러로 불러온 후 matplotlib으로 그레이스케일영상 출력
img = cv2.imread('./dog.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #BGR -> RGB
plt.axis('off')
plt.imshow(img)
plt.show()
'''

# subplot 을 이용하여 왼쪽에는 그레이스케일 영상, 오른쪽에는 컬러영상을 출력
img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('./dog.bmp')
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

plt.subplot(121) #121은 1행2열의 1번쨰 영상 ( = 왼쪽영상)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')

plt.subplot(122)
plt.axis('off')
plt.imshow(img_color)
plt.show()

