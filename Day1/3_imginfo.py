import cv2
import matplotlib.pyplot as plt

img_gray = cv2.imread('./dog.bmp',cv2.IMREAD_GRAYSCALE)
print('img_gray type : ', type(img_gray))
print('img_gray shape : ', img_gray.shape) #(세로, 가로)
print('img_gray dtype : ', img_gray.dtype)

img_color = cv2.imread('./dog.bmp')
print('img_color type : ', type(img_color))
print('img_color shape : ', img_color.shape) #(세로, 가로, 컬러)
print('img_color dtype : ', img_color.dtype)

#문제!! - 아래와 같이 출력하기
#이미지 사이즈 : 548*364
print('img_color shape : ', img_color.shape) #(세로, 가로, 컬러)
width, height, color = img_color.shape
print('이미지사이즈 :', height,'*', width)

#img_color가 그레이스케일 영상인지, 컬러영상인지 구분하기
#if 문을 사용하여 출력

if len(img_color.shape) == 3:
    print('This is color!')
elif len(img_color.shape) == 2:
    print('This is grayscale!')

#img_color에 특정 색 정보로 영상을 변경
#BGR: (255,102,255)
'''
for x in range(height) :
    for y in range(width):
        img_color[x,y] = (255, 102, 255)

cv2.imshow('img_color', img_color)
cv2.waitKey()
'''
img_color[:,:,:] = (255, 102, 255)
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)  #BGR -> RGB
plt.axis('off')
plt.imshow(img_color)
plt.show()


