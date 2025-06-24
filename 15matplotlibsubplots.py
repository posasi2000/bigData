# import matplotlib.pyplot as plt        # 첫번째
# from  matplotlib import pyplot as plt  # 두번째
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)
#----------------------------------------------------------------------------------------------
import numpy as np
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

y1 = [20,50,74,30]   #y축값
y2 = [40, 55,85,60]     #y축값
y3 = np.random.randint(5,35,5) #y축값
y4 = [30,90,10,60,80]

fig, ax = plt.subplots(2, 2, figsize=(12,9))  
ax[0,0].bar(['둘리', '또치', '희동', '도우넛'], y1)
ax[0,0].set_title("악동 둘리친구들")

ax[0,1].scatter(['봄', '겨울', '서머','가을'] , y2 )
ax[0,1].set_title("계절별 고객 동향")

ax[1,0].plot(['레드','블루','그린','자주','노란'] , y3)
ax[1,0].set_title("컬러별 구입현황")

ax[1,1].bar(['aaa','kim','lee','goo','cho'], y4)
ax[1,1].set_title("생성형 AI 이름명명")

fig.suptitle('2025년 국방부 빅데이터 ')
plt.show()
print('그래프 출력 확인 ok ')


