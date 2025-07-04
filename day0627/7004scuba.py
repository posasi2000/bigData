import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import cv2
import time
import numpy as np
#--------------------------------------------------------------------------------------------
# path ='./images/scuba.mp4'
# video = cv2.VideoCapture(path)
# check, frame = video.read()
# cv2.imshow('test', frame)
# cv2.waitKey()
    
# video.release() #동영상을 종료하면 사용했던 메모리 자원을 반환
# cv2.destroyAllWindows()   #모든창 닫기  


# #두번째 실습
path ='./test/scuba.mp4'
video = cv2.VideoCapture(path)

num=0
while video.isOpened():
    check, frame = video.read()
    if not check:
        print('동영상 영상 끝났습니다')
        break
    
    cv2.imshow('test', frame)
    mypath = './test1/myscuba_'+ str(num)+'.jpg'
    cv2.imwrite(mypath, frame)  #myscuba_0.jpg ~ myscuba_218.jpg생성됨
    if cv2.waitKey(25) == ord('q'):
        print('영상을 강제종료합니다')
        break
    num = num + 1

video.release() #동영상을 종료하면 사용했던 메모리 자원을 반환
cv2.destroyAllWindows()   #모든창 닫기 
print('스쿠버 동영상 정상적으로 종료했습니다 ~~~')
print()


