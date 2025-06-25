#플로틀리 사이트 https://plotly.com/python/
import matplotlib.pyplot as plt
from plotly import graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px



import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
print(df)
# print(df.info()) # Date  AAPL.Open  AAPL.High AAPL.Low  AAPL.Close   AAPL.Volume AAPL.Adjusted  dn  mavg   up  direction

# 1번째] ok  Time Series and Date Axes
# fig = go.Figure(data=[go.Candlestick(x=df['Date'],
#                 open=df['AAPL.Open'],
#                 high=df['AAPL.High'],
#                 low=df['AAPL.Low'],
#                 close=df['AAPL.Close'])])

# fig.show()


# 2번째] ok  Time Series and Date Axes
# - 왼쪽이 시작가, 오른쪽이 종가
# - 외국은 붉은색이 하락(<-> 한국은 붉은색이 상승)
# fig = go.Figure(data=[go.Ohlc(x=df['Date'],
#                 open=df['AAPL.Open'],
#                 high=df['AAPL.High'],
#                 low=df['AAPL.Low'],
#                 close=df['AAPL.Close'])])
# fig.update_xaxes(rangeslider_visible=False)
# fig.show()

# https://financedata.github.io/posts/finance-data-reader-users-guide.html
# pip install  finance-datareader  설치하셔야 합니다 
# FinanceDataReader의 DataReader는 미국 주식의 경우 종목코드 대신 티커(Ticker) 사용]
import FinanceDataReader as fdr
FAANG = ["META", "AMZN", "AAPL", "GOOGL"]

# faang_list 의 종가 가져오기
faang_list =  [fdr.DataReader(ticker, "2022")["Close"] for ticker in FAANG]
df_faang = pd.concat(faang_list, axis=1)  #판다스  concat 으로 데이터 병합하기
df_faang.columns = FAANG
df_faang.columns.name = 'company'

# 일별 수익률
df_faang_data = (df_faang / df_faang.iloc[0]) - 1
# fig = px.area(df_faang_data)
# fig = px.line(df_faang_data) #추천
# fig = px.area(df_faang_data, facet_col='company', facet_col_wrap=2)
# fig = px.bar(df_faang_data['META']) #- 사이사이 비어있는 곳은 -> 공휴일 : 장이 안 열린 날 
# fig = px.scatter(df_faang_data, x = 'GOOGL', y = 'AAPL', marginal_x = 'box', marginal_y = 'violin')  #정신없는 형태
# fig = px.scatter_matrix(df_faang_data)  #정신없는 형태
# fig = px.box(df_faang_data, height = 300)
fig = px.histogram(df_faang_data, nbins=50,  facet_col="company", facet_col_wrap=2)
fig.show()

print(df_faang_data.describe())
print()
print(df_faang_data.quantile())



# https://financedata.github.io/posts/finance-data-reader-users-guide.html
print()


























