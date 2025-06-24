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
import numpy as np
import seaborn as sns 
import time

df = pd.DataFrame(
    {'소득':[57327, 93767, 39410, 94951, 59090, 34628, 31809, 46232, 78707, 37816, 47085, 58394, 77072, 97746, 50302, 61129, 83154, 42798, 93530, 84912],
    '교육':[10, 9, 8, 15, 15, 11, 13, 15, 16, 9, 8, 9, 13, 15, 14, 16, 16, 13, 9, 9],
    '태도':[9, 5, 10, 6, 10, 9, 7, 7, 5, 7, 8, 9, 6, 1, 5, 5, 7, 2, 4, 4],
    '투표':[3, 5, 3, 5, 3, 3, 1, 4, 4, 1, 1, 5, 5, 5, 5, 3, 4, 3, 4, 2]
    })

print(df)
print()
print(df.info())
print()

# 해결1] 판다스 상관계수 corr() 
# 해결2] 상관계수를 있으면 피어슨, 무조건 heatmap()열지도 
# 해결3] heapmap() 대각선 1 1 1 기준으로 상오/하왼 동일한 데이터  대각선기준으로 분리 
print('상관계수의 데이터 출력')
print( round(df.corr(),2))
print()
print()

# Pearson 상관계수는 
# -1과 1 사이의 값을 가지며, 1은 완전한 양의 상관, -1은 완전한 음의 상관, 0은 상관이 없음을 의미
corr = round(df.corr(),2)
sns.heatmap(corr,  annot=True , cmap='coolwarm') #cmap='RdBu'
plt.show()


# 해결3] heapmap() 대각선 1 1 1 기준으로 상오/하왼 동일한 데이터  대각선기준으로 분리
#   ㄴ mask = np.zeros_like(corr)
#   ㄴ mask[np.triu_indices_from(mask)] = 1   upper/lower
#   ㄴ 새로운 new_mask  = mask[ 1:, :-1]
#   ㄴ 다시 sns.heapmap()   new_mask1/new_mask2 히트맵열지도에 어떻게 적용 하느냐?

mask = np.zeros_like(corr)
print(mask)
print()

mask[np.triu_indices_from(mask)] = 1 
print(mask)
print('- ' * 30)
print()

print("첫번째 행, 마지막열 제외") 
new_mask1 = mask[1: , :-1] 
new_mask2 = corr.iloc[1: , :-1] 
print(new_mask1)
print()
print(new_mask2)
sns.heatmap(new_mask2,annot=True, mask=new_mask1, cmap='coolwarm')
plt.show()

# 자율4] 그룹화 해서 차트 bar, line, pie
# 02groupby.py문서 참고 
# groupTest3 = df.groupby('국가')['점수'].sum()
# print(groupTest3)
# groupTest3.plot(kind='bar')
# plt.show()
# print()


'''
          소득        교육        태도        투표
소득  1.000000  0.192372 -0.510758  0.598967
교육  0.192372  1.000000 -0.279387  0.346282
태도 -0.510758 -0.279387  1.000000 -0.267829
투표  0.598967  0.346282 -0.267829  1.000000
'''










print()
print()
