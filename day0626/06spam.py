
message = ['spam', 'ham', 'spam', 'ham', 'spam', 'spam', 'ham']
dummy = []
for i in message :
    if i == 'spam' :
        tmp = 1
        dummy.append(tmp)
    elif i == 'ham' : 
        tmp = 0
        dummy.append(tmp)
print('일반식적용', dummy)  # 1  0  1  0  1  1  0
print('리스트축약', [ 1  if k=='spam' else 0  for k in message ] )
print()


squares = [x**2 for x in range(10)]
print('리스트축약', squares)
print()

squares = list(map(lambda x: x**2, range(10)))
print('람다식구현', squares)


"""
일반식적용 [1, 0, 1, 0, 1, 1, 0]
리스트축약 [1, 0, 1, 0, 1, 1, 0]

리스트축약 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

람다식구현 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"""

# 리스트내용 for~ if~elif 한줄표현 list comprehension
# spam 1변환 ham 0변환
# for반복문 if제어문   1  0  1  0  1  1  0
# 함수정의X,  람다식X, 정규식X






















print()
print()