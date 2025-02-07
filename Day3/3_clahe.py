import cv2

img = cv2.imread('./field.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

img_eq = img.copy()
img_clahe = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)

img_eq[:, :, 0] = cv2.equalizeHist(img_eq[:, :, 0])
img_eq = cv2.cvtColor(img_eq, cv2.COLOR_YCrCb2BGR)

# clipLimit: 히스토그램에서 특정 픽셀 값이 지나치게 많이 분포되어 있을 때 이를 제한하여 과도한 대비가 생기지 않도록 함(1~4, 클수록 강한 대비)
# tileGridSize: 블록(타일)으로 나누고 각 타일에 대해 히스토그램 균등화를 개별적으로 수행(너무 작으면 경계가 생기거나 노이즈가 증가, 큰 타일 크기는 부드러운 대비 향상을 가져오지만 디테일을 살리기 어려움)
clahe = cv2.createCLAHE(clipLimit=1, tileGridSize=(4, 4))
img_clahe[:, :, 0] = clahe.apply(img_clahe[:, :, 0])
img_clahe = cv2.cvtColor(img_clahe, cv2.COLOR_YCrCb2BGR)

cv2.imshow('img', img)
cv2.imshow('img_eq', img_eq)
cv2.imshow('img_clahe', img_clahe)
cv2.waitKey()