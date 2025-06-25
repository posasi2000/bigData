
import pandas as pd
import numpy as np
import requests


url = "https://finance.naver.com/api/sise/etfItemList.nhn?etfType=0&targetColumn=market_sum&sortOrder=desc"
print(url) 
print()

# ETF(상장지수펀드)는 기초지수의 성과를 추적하는 것이 목표인 인덱스펀드로, 거래소에 상장되어 있어서 개별주식과 마찬가지로 기존의 주식계좌를 통해 거래
# result = pd.read_html(url, encoding='utf-8')
result = pd.read_json(url, encoding = 'cp949').loc['etfItemList', 'result']
df = pd.DataFrame(result)
print(df)
print('- ' * 60)
print()


response = requests.get(url) #네트워크기본  get 방식임
etf_json = response.json()
print(response.json())
print()
etfItemList = etf_json['result']['etfItemList']
print(etfItemList)
print()
print()

df = pd.DataFrame(etfItemList)
print(df)
print('- ' * 60)
print()

print( df[df['changeRate'] == df['changeRate'].max()] ) # 오늘 가장 크게 오른 종목
print()






