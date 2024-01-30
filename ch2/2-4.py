import cv2 as cv
import sys

#cap=cv.VideoCapture(0,cv.CAP_DSHOW)	# 웹카메라와 연결 시도 cv.VideoCapture(웹 캠 번호->웹 캠 하나: 0, cv.CAP_DSHOW->비디오가 화면에 바로 나타나게 함)
cap=cv.VideoCapture("../ch10/slow_traffic_small.mp4") #동영상 파일과 연결

if not cap.isOpened(): #웹 캠과 연결실패 시 isOpened()함수 false
    sys.exit('카메라 연결 실패')
    
while True:
    ret,frame=cap.read()			# 비디오를 구성하는 프레임 획득 ret에 성공여부 저장, frame에 프레임 저장
                                    #read함수는 호출한 순간의 영상 한장(=프레임)획득&성공여부와 함께 반환
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.') #다 처리했을 때
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #imshow 이전에
    gray_small = cv.resize(gray, dsize=(0, 0), fx=0.5, fy=0.5)

    #cv.imshow('Video display',frame)
    #cv.imshow('Video display', gray)
    cv.imshow('Video display', gray_small)
    
    key=cv.waitKey(1)	# 1밀리초 동안 키보드 입력 기다림
    if key==ord('q'):	# 'q' 키가 들어오면 루프를 빠져나감  ord->아스키코드
        break 
    
cap.release()			# 카메라와 연결을 끊음
cv.destroyAllWindows()