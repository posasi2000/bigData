
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)
import time
# import nltk # nltk.download() # 딱한번만 설치 이미설치하신분들은 주석처리 주석처리
#--------------------------------------------------------------------------------------------
from konlpy.tag import Okt #Open korean text
import urllib.request
import pandas as pd

okt = Okt() ##Open korean text

print('네이버평점 문서 ratings.txt')
urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt", filename="./data/ratings.txt")
train_data = pd.read_table('./data/ratings.txt')
print('train_data.shape ', train_data.shape) #(200000, 3)
print()

print(train_data) #앞뒤 데이터출력
print()


print(train_data.isnull().sum())
print()
"""
id          0
document    8
label       0
"""

train_data = train_data.dropna(how = 'any')  # Null 값이 존재하는 행 제거
print(train_data.isnull().sum()) # 다시  null값 제거 
print(len(train_data)) # 리뷰 개수 출력
print()


# 정규 표현식을 통한 한글 외 문자 제거
train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")

# 불용어 정의
stopwords = ['의','가','이','은','들','는','좀','잘','걍', \
                 '과','도','를','으로','자','에','와','한','하다']


# 형태소 분석기 Twitter를 사용한 토큰화 작업 (오래걸림) 최소 20분
result = []
for n in range(1, 100, 10):
    for sentence in train_data['document']:
        tokenized_sentence = okt.morphs(sentence, stem=True) # 토큰화
        stopwords_removed_sentence = [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
        result.append(stopwords_removed_sentence)
    
    time.sleep(0.1)

print()
# 리뷰 길이 분포 확인
print('리뷰의 최대 길이 :', max(len(review) for review in  result))
print('리뷰의 평균 길이 :',sum(map(len, result))/len(result))
plt.hist([len(review) for review in result], bins=50)
plt.xlabel('length of samples')
plt.ylabel('number of samples')
plt.show()
