#플로틀리 사이트 https://plotly.com/python/
import matplotlib.pyplot as plt
from plotly import graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px

langs = ['python', 'flask', 'css', 'spring', 'jsp']
students = [23, 17, 35, 29, 12]

# x축과 y축에 해당하는 데이터를 각각 넣고 리스트로 감싸줌
# 1번째] ok
# data = [ go.Bar(x = langs, y = students) ]
# fig = go.Figure(data = data)
# fig.show()


# 2번째] ok 붓꽃
# df = px.data.iris()
# print(df) # 3가지의 종류(Setosa, Versicolor, Virginica)
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color='petal_length')
# fig.show()


# 3번째] ok 주식
df = px.data.stocks()
print(df.info())  #date GOOG  AAPL  AMZN FB   NFLX   MSFT 
print(df)

# fig = px.line(df, x = 'date', y = 'GOOG', height= 300)
# fig = px.line(df['GOOG'], height = 300)
# fig = px.line(df.set_index('date'), height = 300)
# fig.show()


# 4번째] ok 주식 Pandas 연결
df_1 = df.set_index('date') - 1
print(df_1)
# df_1.plot(kind = 'bar', figsize = (12, 6))
# plt.show()

# 5번째] ok 주식 Pandas 연결
# fig = px.bar(df_1, height = 300)
# fig.show()

# 6번째] ok 
# px.area로 수익률 분포 그리기
# df_1.columns.name = 'company'
# fig = px.area(df_1, facet_col = 'company', facet_col_wrap = 2)
# fig.show()


# 7번째] ok  여러 종목을 하나의 그래프로 표현
# fig = px.line(df, x = 'date', y= 'GOOG', hover_data={"date": "|%Y-%m-%d"} )
# fig.show()


# 8번째] ok  Time Series and Date Axes
fig = px.line(df_1['GOOG'], title = '구글 주가')
fig.update_xaxes(rangeslider_visible=True)
fig.show()



# https://financedata.github.io/posts/finance-data-reader-users-guide.html

























