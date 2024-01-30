import cv2 as cv

#gray = cv.imread('soccer.jpg', cv.IMREAD_GRAYSCALE)
#cv.imshow('original - gray', gray)

#gray_mask = cv.inRange(gray, 120,170)    # 120~170이면 white, 아니면 black inRange(input이미지,2개의 임계값)
#cv.imshow('inRange', gray_mask)

img = cv.imread('soccer.jpg')
cv.imshow('original', img)

hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
red_mask = cv.inRange(hsv_img,(-10,50,50),(10,255,255))  #red의 범위
img_red = cv.bitwise_and(img, img, mask=red_mask) #red 유효하게 출력
#  A and B : if B=0(black), 0(Black), else(B=1,white) A=0 -> 0, A=1 -> 1

cv.imshow('red detection', img_red)


cv.waitKey()
cv.destroyAllWindows()