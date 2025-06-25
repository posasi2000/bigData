
import pandas as pd
#-------------------------------------------------------------------------------------------
# IQR (Interquartile Range),  z_score개념  원래수치-평균값/분산
#캐글 항공기 https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction

# 해결1] 판다스 df = pd.read_csv(path, encoding='cp949')   행*열 확인 이미해결
# 해결2] 판다스  열 확인하면 Unnamed: 0 제거    해결
# 해결3] pd.info() 이미 해결
# 해결4]  z_scores = [ (x-mean)/std  for x in price금액컬럼] 수식   해결 

# 해결5] 시각화  
# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12,5), sharey=True)
# ㄴ sns.histplot(df, x='price', kde=True,   ax=ax[0]) 도전
# ㄴ sns.histplot(z_scores, x='price', kde=True,   ax=ax[0]) 도전

path = './data/Clean_Dataset.csv'
df = pd.read_csv(path, encoding='cp949')
print(df) #[300,153 rows x 12 columns]   
print()

df.drop(['Unnamed: 0'], axis=1, inplace=True)
print(df.info()) #[300,153 rows x 12 columns]
print()

def my_zscores(df, column):
    z_scores = ( df[column] - df[column].mean()) / df[column].std()
    df_result = df[abs(z_scores) <= 2 ]  #2숫자대신 4, 3 변경 
    return  df_result

dfz_scores =my_zscores(df, 'price' ) #함수호출
print(dfz_scores)
print('이상치 전 ', df.shape)
print('이상치 후 ', dfz_scores.shape)   
# print('이상치제거 갯수' , len(df) - len(dfz_scores))
# 300153 - 289222 = 10,931제거   4


# z_scores = [ (x-mean)/std  for x in data]
# z_scores = [ ( df - mean) /  std  for x in data]
# z_scores = [ ( x - mean) /  std  for x in data]
# IQR = [ x for x, z in zip(data, z_scores)  if abs(z) <= 0.8] 















print()
print()
