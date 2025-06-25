import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='C:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

#--------------------------------------------------------------------------------------------
msg ='한국어 분석을 시작합니다 재미있어요~~'

from konlpy.tag import Kkma
kkma  =  Kkma()
print('from konlpy.tag import Kkma')
print(kkma.sentences(msg))
print(kkma.nouns(msg)) #단어분석 명사추출
print(kkma.pos(msg))   #형태소 분석
print('- ' * 70)
print()

from konlpy.tag import Hannanum
hannanum = Hannanum()
print('from konlpy.tag import Hannanum')
print(hannanum.nouns(msg))
print(hannanum.morphs(msg))
print(hannanum.pos(msg))
print('- ' * 70)
print()


from konlpy.tag import Twitter
twitter = Twitter()
print('from konlpy.tag import Twitter')
print(twitter.nouns(msg))
print(twitter.morphs(msg))
print(twitter.pos(msg)) #[('한국어', 'Noun'), ('분석', 'Noun'), ('을', 'Josa'), ('시작', 'Noun'), ('합니다', 'Verb'), ('재미있어요', 'Adjective'), ('~~', 'Punctuation')]
print(twitter.pos(msg, norm=True, stem=True))
print(twitter.pos(msg, norm=False, stem=False))
print('- ' * 70)
print()


from konlpy.tag import Okt  #Open korean text
okt = Okt()
print('from konlpy.tag import Okt ')
print(okt.nouns(msg))
print(okt.morphs(msg))
print(okt.pos(msg))
print(okt.phrases(msg))
print('- ' * 70)
print()

msg ='한국어 분석을 시작합니다 재미있어요~~'



"""
ModuleNotFoundError: No module named 'konlpy'
ModuleNotFoundError: No module named 'wordcloud'  아나콘다에 nltk기본으로 설치되어 있음
ModuleNotFoundError: No module named 'nltk'       아나콘다에 nltk기본으로 설치되어 있음
pip install konlpy
pip install wordcloud
생략 pip install nltk
그런데 nltk.download() 최초한번만 설치하고 주석처리 
"""

print()
print()