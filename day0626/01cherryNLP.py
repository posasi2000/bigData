import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='C:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

#--------------------------------------------------------------------------------------------
from wordcloud import WordCloud, STOPWORDS
"""
pos(part of  speech)  문장의 형태소를 구분 어근,접미,접두,폼사속성
KoNLPy의 말뭉치(corpus)
 Hannanum KAIST  : 말뭉치를 이용해 생성된 사전
 Kkma : 세종 말뭉치를 이용해 생성된 사전(꼬꼬마)
 Mecab : 비권장 세종 말뭉치로 만들어진 CSV 형태의 사전
 Komoran : Java로 쓰여진 오픈소스 한글 형태소 분석기
 Twitter(Okt): 오픈 소스 한글 형태소 분석기  #Okt = Open korean text

wc = WordCloud(글꼴크기, 불용어, 글꼴, 바탕색, 가로, 높이, colormap='') #시각화 차트,맵,워드클라우드
wc.generate(msg실제내용)
그래프처럼연결 plt.show()
워드클라우드는 konlpy의 말뭉치랑 연결안해도 가능 


- KoNLPy=코엔엘파이  
 파이썬 한국어 형태소 분석 라이브러리 사용후 시각화 WordCloud
"""

msg='''  
cherry 제리톰 우박 cherry 금요일 leurto 우박 adslfj 가을 cherry 금요일  bigdata 와
일요일 sld 제리 jfldf 금요일 leurto  monday  봄 여름 가을 겨울톰톰 우박
일요일 우박 803 ldfjlqwewtry 우박 upu fdgjld 이  우박
cherry 일요일 sld cherry bigdata 금요일 leurto 우박  bigdata 
monday 우박 weoripti  우박 cherry 제리와톰  bigdata  도
monday 제리와톰톰 가을 koetiet 9734 234 금요일 톰 제리톰 adslfj cherry 금요일 우박
bc 우박 금요일 하늘 bigdata 금요일 eirp cherry weoripti 금요일 
금요일  upu 우박
cherry  cherry 우박  bigdata 톰과제리    
'''

# 불용어 정의
mystop = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다', '그','너','나','테','니','뇨',]
stopwords = set(STOPWORDS)
for i in mystop:
    stopwords.add(i)

# stopwords.add('우박') 
# stopwords.update(['목요일', '천둥번개'])   #불용어 대상추가  
wc = WordCloud(stopwords=stopwords, width=800, height=800, colormap = 'Accent_r',
               font_path='C:/windows/Fonts/malgun.ttf', background_color='white' )
wc.generate(msg)

plt.imshow(wc)
plt.axis('off')
plt.show()

"""
pos(part of  speech)  문장의 형태소를 구분 어근,접미,접두,폼사속성
KoNLPy의 말뭉치(corpus)
 Hannanum KAIST  : 말뭉치를 이용해 생성된 사전
 Kkma : 세종 말뭉치를 이용해 생성된 사전(꼬꼬마)
 Mecab : 비권장 세종 말뭉치로 만들어진 CSV 형태의 사전
 Komoran : Java로 쓰여진 오픈소스 한글 형태소 분석기
 Twitter(Okt): 오픈 소스 한글 형태소 분석기   #Okt = Open korean text

 
ModuleNotFoundError: No module named 'konlpy'
ModuleNotFoundError: No module named 'wordcloud'  아나콘다에 nltk기본으로 설치되어 있음
ModuleNotFoundError: No module named 'nltk'       아나콘다에 nltk기본으로 설치되어 있음
pip install konlpy
pip install wordcloud
생략 pip install nltk
그런데 nltk.download() 최초한번만 설치하고 주석처리 


pip install  numpy  pandas  matplotlib  seaborn    
pip install  nltk  openpyxl   lxml    html5lib  
pip install  geopy
pip install  geopandas  
pip install  urllib.request
pip install  json

restAPI = Representational State Transfer application
"""

print()
print()