import cv2
#오버레이 이미지는 png파일이여야 하고 배경이 투명인걸 선호해야 한다.
img = cv2.imread('01.jpg')
overlay_img = cv2.imread('dices.png', cv2.IMREAD_UNCHANGED)
#png파일을 사용할때는 투명도를 같이 로드하고 싶어서 imread를 부른다


#3개의채널로는 색깔만 표현할수있고 채널이 하나추가 (A(알파))채널은 투명도를 표현하는 채널이다.
overlay_img = cv2.resize(overlay_img, dsize=(150, 150))

#이미지합성 함수부분
overlay_alpha = overlay_img[:, :, 3:] / 255.0
background_alpha = 1.0 - overlay_alpha

x1 = 100
y1 = 100
#주사위 이미지를 넣고싶은 왼쪽위 좌표
x2 = x1 + 150
y2 = y1 + 150
#위의 dsize150 150 이라서 x2,y2도 똑같이 150,150더해준다
img[y1:y2, x1:x2] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * img[y1:y2, x1:x2]

cv2.imshow('img',img)
cv2.waitKey(0)
#계속띄워놓을거야