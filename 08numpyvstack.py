import numpy as np


x = np.array([1, 2, 3])   #1행3열
y = np.array([7, 8, 9])   #1행3열

print( np.vstack((x,y)) ) #[ [1 2 3]  [7 8 9] ]   
print()

print( np.hstack((x,y)) ) #[  1 2 3 7 8 9 ]   왼쪽에서 오른쪽 1행 * 6열
print()

print( np.concatenate((x,y), axis=0) )  # [  1 2 3 7 8 9 ]   왼쪽에서 오른쪽 1행 * 6열
print('- ' * 60)
print()
# 에러 print( np.concatenate((x,y), axis=1) )  #numpy.exceptions.AxisError: axis 1 is out of bounds for array of dimension 1


#첫번째 실습 seed = 1234
# np.standard_normal()는 평균이 0이고 표준 편차가 1인 정규 분포에서 샘플을 추출
rng = np.random.default_rng(seed = 42)
myarray = rng.standard_normal( (5,4) ) # 5행 * 4열
print(myarray)
print()
print('myarray정보 shape ', myarray.shape) #shape()에러
print('myarray정보 ndim ', myarray.ndim,'차원')   #2차원 형태 Array
print('myarray정보 size()', myarray.size) # 5*4=20
print('myarray정보 len() ', len(myarray)) #행길이 
print()
print('평균' , myarray.mean())
print('평균', np.mean(myarray))
print()
print('열평균' , myarray.mean(axis=0))  #열세로
print('행평균' , myarray.mean(axis=1))  #행가로
 
"""
42는 특별히 디지털 문화에서 유명한 숫자입니다. 
그 기원은 더글라스 아담스의 소설 "The Hitchhiker's Guide to the Galaxy"에서 유래합니다. 소설에서 "우주와 모든 것에 대한 궁극적인 질문의 답은 42"라고 언급됩니다. 
그 이후로 42는 종종 무의미한 숫자로, 재미로 사용되곤 합니다.
"""

















print()