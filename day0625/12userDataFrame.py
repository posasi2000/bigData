import pandas as pd
import numpy as np
# 데이터건 10000건, 10만건 쉽게 생성하는 방법 

np.random.seed(42)
num_records  = 10000
num_users = 1000
num_items = 2000
data = {
    'user_id': np.random.randint(1, num_users + 1, num_records),
    'item_id': np.random.randint(1, num_items + 1, num_records),
    'feature_1': np.random.random(num_records),
    'feature_2': np.random.random(num_records),
    'feature_3': np.random.random(num_records),
    'feature_4': np.random.random(num_records),
    'target': np.random.randint(0, 2, num_records)  # 0 또는 1
}

df = pd.DataFrame(data) # 데이터프레임 생성
print(df)
df.to_csv('./data2/user_item_data.csv', index=False) # CSV 파일로 저장
print("./data2/user_item_data.csv 생성 완료 성공했습니다")
print()















print()
print()