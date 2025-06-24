import numpy as np


print(np.zeros(10)) #0실수값으로 채워짐
print(np.ones(10))  #1실수값으로 채워짐
print()

print(np.zeros([4,6]))
print()
print(np.ones([4,6]))
print()
print('- ' * 35)

z = np.full( (4,6), 0) #0숫자를 4행x6열
print(z)
print()

z = np.full( (4,6), 78) #78숫자를 4행x6열
print(z)
print()

z = np.full( (4,6), 'e') #'e' 4행x6열
print(z)
print()

print('eye윙크느낌 ') 
z = np.eye(4,6)
print(z)
print()


print('unique적용')
a = np.array( [9,5,4,3,1,2,3,4,3,2,4,1,2,3,7,3,1,2,1,2,5,1,7,1,2,2,1,3] )
ret = np.unique(a)  #[1 2 3 4 5 7 9]
print(ret)
print()

print('trim zero숫자처리')
b = np.array( [0,0,0,0,0,3,0,2,3,4,0,2,4,1,2,3,7,3,1,2,0,0,5,1,7,1,0,0,0,0] )
print(np.trim_zeros(b))
print(np.trim_zeros(b, trim='f')) #front-end
print(np.trim_zeros(b, trim='b')) #back-end
print(np.trim_zeros(b, trim='bf'))
print('- ' * 60)
print()


a = np.array( [ [1,2], [3,4] ] )  
b = np.array( [ [5,6], [7,8] ] ) 

print(np.vstack((a,b))) #데이터를 왼쪽에서 오른쪽
print()

print(np.hstack((a,b)))  #데이터를 위에서 아래로  # [ [1 2 5 6]  [3 4 7 8]]
print('- ' * 60)
print()


c = np.array( ( [74,56,14], [900,800,900]) )
print(c)
print()

print(np.transpose(c))  # c.T 같음
print()
print(c.T)  # np.transpose(c) 같음 , 과일데이터 그래프에서 사용
print()
print()


import time
y = np.arange(16).reshape(4,4) #4행 * 4열
print(y)
print()
print('trace대각선 숫자 더하기연산 ')
print(np.trace(y)) # 30 = 0 + 5 + 10 + 15
print()
print()

time.sleep(1)
z = np.arange(27).reshape(3,3,3)
print(z)
print('\n두번째trace()') 
print(np.trace(z)) # [36 39 42]
# [(0+12+24) ,(1+13+25) , (2+14+26)  ] = [36 39 42]

# https://velog.io/@dev_dreamer/데이터-시각화-Plotly-사용법
# https://moruxz.tistory.com/76


"""
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
"""



# 행렬 = matrix
# 넘피Numpy에서 자주사용 되는 선형대수 함수
# matrix는 행렬
"""
단위행렬(Unit matrix): np.eye(n)
영행렬(Zaro matrix): np.zeros((m, n))
대각행렬(Diagonal matrix): np.diag(x)
전치행렬(Transpose matrix): np.T, np.transpose(a)
내적(Dot product, inner product): np.dot(a, b)
대각합(trace): np.trace(x)
행렬식(Matrix Determinant): np.linalg.det(x)
역행렬(Inverse of a matrix): np.linalg.inv(x)
고유값(Eigenvalue), 고유백터(Eigenvector): w, v = np.linalg.eig(x)
특잇값 분해(Singular Value Decomposition): u, s, vh = np.linalg.svd(A)
연립방정식 해 풀기: np.linalg.solve(a, b)
최소자승 해 풀기: m, c = np.linalg.lstsq(A, y, rcond=None)
"""

# 변수이름및 함수이름 규칙 camelCase권장
# snake_case
# camelCase
# PascalCase
# kebab-case

print()