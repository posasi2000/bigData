import pandas as pd

df = pd.DataFrame({
    'weight' : [ 80.0, 76.0, 46.7, 51.2, 87.9, 65.4] ,
    'height' : [ 170, 180, 156, 160, 190, 164],
    'gender' : ['m','f', 'm', 'f', 'm','m']
 })
print(df)
print()
print()

#해결1]  index 2 3 열은 전체
print('\n2행 3행 모든열포함추출')
print(df[2:4])
print()

#해결2] weight컬럼의 데이터 추출
# print(df.weight) 
# print(df["weight"] )
print(df[ ["weight"] ])  # 데이터및 컬럼이름까지 출력 
'''
   weight
0    80.0
1    76.0
2    46.7
3    51.2
4    78.9
5    65.4
'''

print()

#해결3] sort=숫자데이터 적용하면 편합니다 
print(df.sort_values(by='weight'))
print()
print(df.sort_values(by='weight', ignore_index=True))
print()
#해결4] sort=숫자데이터 weight열   자동 오름차순  순번 index번호 유지
#해결5] sort=숫자데이터 weight열   내림차순  순번 index번호 유지
print(df.sort_values(by='weight', ascending=False,  ignore_index=True))
print()

#해결6] 성별 gender그룹화  groupby키워드 사용
#  ㄴ 해결 for반복문으로  df_group
df_group = df.groupby('gender')
print(df_group) #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000018F7F2DE090>
for key, gg in df_group:
    print(key, ' ' , gg)
    print('- ' * 30)
print()

#해결7] 성별 weight컬럼, height컬럼  평균mean()구해서 gender컬럼그룹화 
print('gender그룹화')
df_group_mean = df_group.mean()
print(df_group_mean)

'''
   weight  height gender
0    80.0     170      m
1    76.0     180      f
2    46.7     156      m
3    51.2     160      f
4    87.9     190      m
5    65.4     164      m
'''





print()
