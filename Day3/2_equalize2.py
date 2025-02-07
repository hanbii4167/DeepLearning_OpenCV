import cv2

img = cv2.imread('./field.bmp')

'''
ycrcb=[]
dst = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
ycrcb = cv2.split(dst)
ycrcb = list(ycrcb) # ycrcb 는 튜플로 떨어져서 리스트로 변환해줘야한다
#print(ycrcb)

ycrcb[0] = cv2.equalizeHist(ycrcb[0])v #평탄화
dst = cv2.merge(ycrcb)
dst = cv2.cvtColor(dst, cv2.COLOR_YCrCb2BGR)

cv2.imshow('img',img)
cv2.imshow('dst', dst)
cv2.waitKey()
'''

#split() 와 merge() 를 사용하지 않고 위 예제와 동일한 결과 영상을 만들어보자

ycrcb=[]
dst = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
dst = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)


cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
