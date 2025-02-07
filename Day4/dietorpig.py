from random import random

import cv2
import random


img1 = cv2.imread('./pig.png')
img2 = cv2.imread('./diet.png')

user_input = input(" 다이어트할까 하지말까?ㅋ : ")

if user_input.lower() == '골라주셈!':
    # 이미지 중 하나를 랜덤으로 선택
    selected_img = random.choice([img1, img2])

    # 선택된 이미지 표시
    cv2.imshow('Selected Image', selected_img)
    cv2.waitKey(0)  # 키 입력이 있을 때까지 대기
    cv2.destroyAllWindows()  # 모든 창 닫기
else:
    print("You didn't type 'start'.")