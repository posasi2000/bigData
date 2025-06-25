
import matplotlib.pyplot as plt

#플로틀리 사이트 https://plotly.com/python/
from plotly import graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

langs = ['python', 'flask', 'css', 'spring', 'jsp']
students = [23, 17, 35, 29, 12]

# x축과 y축에 해당하는 데이터를 각각 넣고 리스트로 감싸줌
# 1번째] ok
# data = [ go.Bar(x = langs, y = students) ]
# fig = go.Figure(data = data)
# fig.show()



# 2번째] ok
"""
branches = ['CSE', 'Mech', 'Electronics']
fy=[23, 17, 35]
sy=[20, 23, 30]
ty=[30, 20, 15]

# x는 동일하되 y의 값은 다른 3개의 Bar객체 생성
trace1=go.Bar(
    x = branches,
    y = fy,
    name = 'FY1')

trace2=go.Bar(
    x = branches,
    y = sy,
    name = 'SY2')

trace3=go.Bar(
    x = branches,
    y = ty,
    name = 'TY3')

data = [trace1,trace2,trace3]

# 그룹화 된 막대 차트를 표시하려면 레이아웃 개체의 막대 모드 속성을 그룹으로 설정해야함
layout = go.Layout(barmode='group',title='Departments')
fig = go.Figure(data=data,layout=layout)
fig.show()
"""


# 3번째] ok
"""
langs = ['python', 'flask', 'css', 'spring', 'jsp']
students = [23, 17, 35, 29, 12]

data = [go.Pie(
    labels = langs,
    values = students,
    # 각각의 인덱스에 배정된 조각을 원점을 기준으로 얼마나 당길건지 설정
    pull=[0.1,0,0,0,0]
)]

fig = go.Figure(data=data)
fig.show()
"""


# 4번째] ok
"""
countries = ["USA", "China", "European", "Korea", "Brazil", "India", "Rest of World"]
ghg = [16, 15, 12, 6, 5, 4, 42] 
co2 = [27, 11, 25, 8, 1, 3, 25]

fig = make_subplots(rows=1,cols=2, 
                    specs=[[{'type':'domain'},{'type':'domain'}]]) # 1x2형식의 subplot 생성
fig.add_trace(go.Pie(labels=countries,
                    values=ghg,
                    name="GHG Emissions"),
             # 1행 1열에 위치
             row=1,col=1)

fig.add_trace(go.Pie(labels=countries,
                    values=co2,
                    name="CO2 Emissions"),
             # 1행 2열에 위치
             row=1,col=2)

# hole은 파이차트 가운데 구멍의 크기를 설정
# hoverinfo는 마우스 커서를 갖다 댔을때 띄워질 정보 설정
fig.update_traces(hole=0.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="Global Emissions 1990-2011", # 타이틀 설정
    # annotations은 주석에 대한 정보를 딕셔너리형태로 표현하고 리스트에 넣어서 전달 받음.
    # showarrow가 True면 해당좌표를 화살표로 가리킴.
    annotations=[dict(text='GHG',x=0.19, y=0.5, font_size=20, showarrow=False),
                 dict(text='CO2',x=0.8, y=0.5, font_size=20, showarrow=False)])

fig.show()
"""


# 5번째] ok
# np.random.seed(1)
# x = np.random.randn(500) # 표준 정규분포를 따르는 난수 500개를 ndarray로 반환
# data=[go.Histogram(x=x)]
# fig=go.Figure(data)
# fig.show()


x0=np.random.randn(500)
x1=np.random.randn(500)+1

fig=go.Figure()
# go.Figure(data = []) 방법이 아닌 add_trace 메소드를 통해 직접 Trace를 추가할 수도 있음
fig.add_trace(go.Histogram(x=x0))
fig.add_trace(go.Histogram(x=x1))

# 중첩해서 표현
fig.update_layout(barmode='overlay')
# 중첩해서 보여주기 위해 불투명도 설정(각각의 trace에서 따로 설정가능)
fig.update_traces(opacity=0.75) #생략하면 2개 히스토
fig.show()


# 6번째] ok 이상치에 많이 사용
# Box Plots은 주로 데이터에서 이상치를 탐지하는데 사용한다.
# q1은 하위 25%를 의미하고 q3는 상위 25%를 의미한다.
# yaxis = [1140,1460,489,594,502,508,370,200] 
# data = go.Box(y = yaxis) 
# fig = go.Figure(data) 
# fig.show()


