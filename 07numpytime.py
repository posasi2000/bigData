import numpy as np
import time

# 넘피 이용 연산처리 권장 
# start = time.time()
# print('넘피 이용한 * 2 연산 1~1000000')
# my_arr = np.arange(1,1_000_001) 
# my_arr2 = my_arr * 2
# print(my_arr2)
# print()
# end = time.time()
# cal = end-start
# print(f'시간차 =  {cal}초')  #시간차 =  0.0014379024505615234초
# print()


start = time.time()
print('일반 list를 이용한 * 2 연산  1~1000000')
my_list = list(range(1, 1_000_001)) 
my_list2 = [x * 2 for x in my_list] 
print(my_list2)
end = time.time()
cal = end-start
print(f'시간차 =  {cal}초')  # 시간차 =  1.6403615474700928초


# 이미지numpy.png이미지 
