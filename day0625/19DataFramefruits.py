# import matplotlib
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

import pandas as pd
import time

fruits = ['orange', 'cherry', 'gold', 'kiwi']  #index 데이터 이용
area = ['제주', '안양', '수원', '일산'] 
su1 = [21,  34,  45,  13]
su2 = [45,  19,  31,  50]
su3 = [33,  56,  27,  41]
su4 = [77,  26,  65,  29]

# 해결2] 판다스 DataFrame화 df = pd.DataFrame(  ) 
#  ㄴ 지역area 키값  , index값으로 fruits과일 품목 
#  ㄴ su1 ~ su4 리스트데이터 value
df = pd.DataFrame( { area[0]:su1, area[1]:su2,  area[2]:su3, area[3]:su4} ,index=fruits)  
print(df)
print()

# 해결3] df대상으로 bar타입 그래프 생성
# 해결4] 데이터값표시  plt.text()
ax = df.plot(kind='bar', figsize=(10,7))
for k in range(len(ax.patches)):
    rect = ax.patches[k]
    print(k, '번째  ', rect)
    plt.text(rect.xy[0], rect.get_height(), str(rect.get_height()), fontsize=12)

plt.show() 
time.sleep(1)

#--------------------------------------------------------------------------------------
dft = df.T  #09numpy.py문서
ax = dft.plot(kind='bar', figsize=(10,7))
for k in range(len(ax.patches)):
    rect = ax.patches[k]
    print(k, '번째  ', rect)
    plt.text(rect.xy[0], rect.get_height(), str(rect.get_height()), fontsize=12)

plt.show() 
# http://seaborn.pydata.org/







