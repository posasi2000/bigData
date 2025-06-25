import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='C:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)


from konlpy.tag import Okt  #Open korean text
okt = Okt()
#--------------------------------------------------------------------------------------------
import nltk # 딱 1회만 처리 nltk.download() 매번할때마다 다운로드하면 민폐
'''
토큰의 이해  문맥,문장,워드를 품사화 pos 
NLP처리에서 텍스트의  의미 있는 단위로 분리하는 작업 토큰 = tokenization(word토큰, sentence토큰) 
'''

msg = "Garbage in, Garbage out"
sentence = "Garbage in, Garbage out"

# 순서1] 파이썬 문장분리 기본함수 문장분리=토큰의 시작  split()분리대신 토근화
print('순서1 split')
tokens  = [ x for x in sentence.split(' ') ]
print(tokens) 
print()


# 순서2] 정제화 cleaning 
print('순서2 정제화')
sentence = sentence.replace("," , "")
tokens  = [ x for x in sentence.split(' ') ]
print(tokens) 
print()
print()

msg = "I like to pet the cat's soft fur."
# 순서3] nltk라이브러리 사용 word_tokenize
print('순서3 nltk word_tokenize')
from nltk.tokenize import word_tokenize
tokens  = word_tokenize(msg)
print(tokens) 

sentence = "Don't waste your youth. you're not always young"
tokens = word_tokenize(sentence)
print(tokens)
print()



# 순서4] nltk라이브러리 사용 TreebankWordTokenizer
print('순서4 nltk TreebankWordTokenizer')
from nltk.tokenize import TreebankWordTokenizer
treebank = TreebankWordTokenizer()
tokens1 = treebank.tokenize(msg)
tokens2 = treebank.tokenize(sentence)
print(tokens1)
print(tokens2)
print()

# 순서5] nltk라이브러리대신 textblob  pip install TextBlob
print('순서5 nltk대신 TextBlob')
from textblob  import TextBlob
tokens1 = TextBlob(msg)
tokens2 = TextBlob(sentence)
print(tokens1.words)  
print(tokens2.words)  
print()


msg = "I like to pet the cat's soft fur."
sentence = "Don't waste your youth. you're not always young"
# 순서6] nltk라이브러리 RegexpTokenizer, 정규식표현적용
print('순서6 nltk RegexpTokenizer')
from nltk.tokenize import RegexpTokenizer
regexp = RegexpTokenizer('[\w]+') #원본
# regexp = RegexpTokenizer('[\s]+', gaps=True)
tokens1 = regexp.tokenize(msg)
tokens2 = regexp.tokenize(sentence)
print(tokens1)
print(tokens2)
print()

"""
regexp = RegexpTokenizer('[\w]+')
['I', 'like', 'to', 'pet', 'the', 'cat', 's', 'soft', 'fur']
['Don', 't', 'waste', 'your', 'youth', 'you', 're', 'not', 'always', 'young']

regexp = RegexpTokenizer('[\s]+', gaps=True) 아래 결과값 출력
['I', 'like', 'to', 'pet', 'the', "cat's", 'soft', 'fur.']
["Don't", 'waste', 'your', 'youth.', "you're", 'not', 'always', 'young']
"""








print()
print()