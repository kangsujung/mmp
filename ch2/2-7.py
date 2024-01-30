import cv2 as cv
import sys

img=cv.imread('girl_laughing.jpg') 
  
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
def draw(event,x,y,flags,param):		# 콜백 함수(이벤트종류, 이벤트가 일어난 순간의 커서 위치,특수키(shift,ctrl,alt),param)
    if event==cv.EVENT_LBUTTONDOWN:	# 마우스 왼쪽 버튼 클릭했을 때
        cv.rectangle(img,(x,y),(x+200,y+200),(0,0,255),2)
    elif event==cv.EVENT_RBUTTONDOWN:	# 마우스 오른쪽 버튼 클릭했을 때
        cv.rectangle(img,(x,y),(x+100,y+100),(255,0,0),2)  
        
    cv.imshow('Drawing',img)           #바뀐 영상 윈도우에 반영
    
cv.namedWindow('Drawing') #윈도우에 이름붙여서 생성
cv.imshow('Drawing',img) #윈도우에 img영상 디스플레이

cv.setMouseCallback('Drawing',draw)	# Drawing 윈도우에서 마우스이벤트발생하면 draw 콜백 함수 호출하라고 지정

while(True):		# 마우스 이벤트가 언제 발생할지 모르므로 무한 반복=>프로그램 실행 지속 *??1초동안 키보드입력 기다리는 것을 무한반복
    if cv.waitKey(1)==ord('q'): #프로그램 종료
        cv.destroyAllWindows() 
        break