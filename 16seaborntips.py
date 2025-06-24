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
# http://seaborn.pydata.org/tutorial/introduction.html
sns.set_theme()
tips = sns.load_dataset('tips')
print(tips) # total_bill   tip   sex smoker   day   time  size
print()


sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size"
)
plt.show()

# total_bill   tip   sex smoker   day   time  size
sns.displot(tips, x='total_bill', col='time', kde=True )
plt.show()

# total_bill   tip   sex smoker   day   time  size
sns.catplot(tips,  kind='bar', x='day', y='total_bill', hue='smoker' )
plt.show()

sns.scatterplot(data=tips,	x="total_bill",	y="tip",	hue="time")
plt.show()

sns.histplot(data=tips,	x="total_bill",	kde=True)  # 권장  # KDE는 커널 밀도 추정(Kernel Density Estimation) 
plt.show()

tips = sns.load_dataset('tips')
corr = tips.corr(numeric_only=True) # 피어슨, 스피어만, 켄달 
sns.heatmap(corr, annot=True, cmap='coolwarm')  #cmap='RdBu'
plt.show()
print()

# KDE는 커널 밀도 추정(Kernel Density Estimation) 
# hue는 데이터의 구분 기준을 정하여 색상을 통해 구분
# 색조Hue=색상,  명도Brighgt 0~100, 채도saturation 


