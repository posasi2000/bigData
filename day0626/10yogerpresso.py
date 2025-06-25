
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
import folium
import os
import webbrowser
import seaborn as sns 
#-----------------------------------------------------------------------------------------------

df = pd.read_csv('data/소상공인시장진흥공단_상가(상권)정보_서울_202109.csv')
print()
# print(df)
print(df.info()) 
# 상가업소번호 상호명  지점명 상권업종대분류코드 상권업종대분류명 상권업종중분류코드  상권업종중분류명 
# 상권업종소분류코드  상권업종소분류명  건물명  도로명주소  ~  경도  위도
print()

m = folium.Map([37.5671, 126.9774],zoom_start=11)

for k in range(len(df)):
    location = (float(df.loc[k,'위도']),float(df.loc[k,'경도']))
    name = str(df.loc[k,'상호명'])
    if '요거프레소' in name:
        if name == '요거프레소':
            if str(df.loc[k,'지점명'])!='nan':
                name = name + str(df.loc[k,'지점명'])
        popup = folium.Popup(name+'\n'+str(df.loc[k,'도로명주소']), min_width=50, max_width=200)
        folium.Marker(location, popup=popup, tooltip=name, icon=folium.Icon(icon='mug-hot',color='black',prefix='fa')).add_to(m)

path = 'data/yogerpresso1.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print()


cnty  = df['상권업종대분류명'].value_counts()
print(cnty)
print()

cntx  = df['상권업종대분류명'].value_counts().index
print(cntx)
print()

plt.figure(figsize=(12,7))
plt.bar(cntx, cnty)
plt.title('소상공인 상권업종 대분류명 bar차트 ')
plt.show()


plt.figure(figsize=(10,6))
sns.barplot(x=cntx, y=cnty, color='green', palette='Set1')  # palette='pastel'
plt.title('소상공인 상권업종 대분류명 barplot 차트 ')
plt.show()
