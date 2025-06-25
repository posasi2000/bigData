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
import seaborn as sns 
import time
import json
import requests  
import folium
import os
import webbrowser


path = './data/소상공인시장진흥공단_상가(상권)정보_서울_202109.csv'
df = pd.read_csv(path, encoding='utf-8')  
# print(df)  #[325,880 rows x 39 columns]
print('- ' * 40)
print()
# print(df.info())
# print()
'''
 #   Column     Non-Null Count   Dtype
---  ------     --------------   -----
 0   상가업소번호     325880 non-null  int64
 1   상호명        325879 non-null  object
 2   지점명        59613 non-null   object
 3   상권업종대분류코드  325880 non-null  object
 4   상권업종대분류명   325880 non-null  object
 5   상권업종중분류코드  325880 non-null  object
 6   상권업종중분류명   325880 non-null  object
 7   ~~~ 30, 32 ~ 36 필드생략 
 31  도로명주소      325880 non-null  object
 37  경도         325880 non-null  float64
 38  위도         325880 non-null  float64
'''


# 순서1] 상권업종대분류명
cnty  = df['상권업종대분류명'].value_counts()
print(cnty)
print()

cntx  = df['상권업종대분류명'].value_counts().index
print(cntx)
print()

# 순서2] 차트표시
#일반matplotlib
plt.figure(figsize=(12,7))
plt.bar(cntx, cnty)
plt.title('소상공인 상권업종 대분류명 bar차트 ')
plt.show()

# seaborn차트
plt.figure(figsize=(10,6))
sns.barplot(x=cntx, y=cnty, color='green', palette='Set1')  # palette='pastel'
plt.title('소상공인 상권업종 대분류명 barplot 차트 ')
plt.show()


# 순서3] 상호명 던킨도너츠 , EDIYACOFFEE, 이디야커피(이디아) ediyacoffee , 요거프레소  가져오기
# ediya=df[ df['상호명'].str.contains('이디야커피|이디아커피|이디아|ediya|EDIYACOFFEE', na=False) ]
# ediya=df[ df['상호명'].str.contains('ediya|EDIYACOFFEE', na=False) ]
# print(ediya)

# df['상호명_lower'] = df['상호명'].str.lower() #상호명 영문을 전체 소문자화
# ediya=df[ df['상호명_lower'].str.contains('ediya|ediyacoffee|이디아|이디야', na=False) ]
# print(ediya) #[479 rows x 40 columns]

# df['상호명_lower'] = df['상호명'].str.lower() #상호명 영문을 전체 소문자화
# yoger=df[ df['상호명_lower'].str.contains('yogerpresso|요거프레소|요거 프레소|yoger presso', na=False) ]
# print(yoger) #[75 rows x 40 columns]


df['상호명_lower'] = df['상호명'].str.lower() #상호명 영문을 전체 소문자화
star=df[ df['상호명_lower'].str.contains('STARBUCKS|스타벅스|스타 벅스', na=False) ]
print(star) #[507 rows x 40 columns]


m = folium.Map(location=[37.5671, 126.9774], zoom_start=11)
latlong = star[['위도', '경도']] 

from folium.plugins import MarkerCluster
mc_cluster  = MarkerCluster().add_to(m)

for lat,long in zip(latlong['위도'], latlong['경도']):
    folium.Marker([lat,long],icon=folium.Icon(icon='mug-hot', color='black', prefix='fa')).add_to(mc_cluster)


# https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
request = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
seoul_geo =  json.loads(request.content)
folium.GeoJson(seoul_geo , name='서울구역표시').add_to(m)

print('testing1...')
m.save('./data/star.html')
webbrowser.open(os.path.realpath('./data/star2.html'))
print('star.html 스벅  밀도해결  ') 



print('testing2...완전답답')
time.sleep(3)
for k in star.index:
    print()
    k_lat = star.loc[k, '위도']
    k_long = star.loc[k, '경도']
    folium.Marker([k_lat,k_long], icon=folium.Icon(color='red')).add_to(m)

path ='./data/star2.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('star2.html  지도출력 testing...')




print('testing3...완전답답')
time.sleep(3)
for k in range(len(df)):
    location = (float(df.loc[k,'위도']),float(df.loc[k,'경도']))
    name = str(df.loc[k,'상호명'])
    if '스타벅스' in name:
        if name == '스타벅스':
            if str(df.loc[k,'지점명'])!='nan':
                name = name + str(df.loc[k,'지점명'])
        popup = folium.Popup(name+'\n'+str(df.loc[k,'도로명주소']), min_width=50, max_width=200)
        folium.Marker(location, popup=popup, tooltip=name, icon=folium.Icon(icon='mug-hot',color='black',prefix='fa')).add_to(m)

path = 'data/star3.html'
m.save(path)
webbrowser.open(os.path.realpath(path))
print('star3.html  지도출력 testing...')





print()
print()