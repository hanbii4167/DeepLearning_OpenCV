import cv2

img= cv2.imread('./dog.bmp')
cv2.imshow('img',img)
# cv2.waitKey()

while True:
    keyvalue = cv2.waitKey()
    if keyvalue ==ord('i') or keyvalue == ord('I'): #아스키코드 값 알 수 있다.
        img = ~img #영상 반전
        cv2.imshow('img',img)
    elif keyvalue ==27:
        break # esc 누르면 종료