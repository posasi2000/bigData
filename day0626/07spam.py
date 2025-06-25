
message = ['spam', 'ham', 'spam', 'ham', 'spam', 'spam', 'ham']

# 리스트컴프리핸션 적용해서 ham출력
print('리스트축약', [ 1  if k=='spam' else 0  for k in message ] ) # 리스트축약 [1, 0, 1, 0, 1, 1, 0]
print('리스트축약', [ k  for k in message if k == 'ham' ] )
print('리스트축약', [ k  for k in message if 'ham' in k ] )
print('리스트축약', [ x  for x in range(1,11) if x%2 == 0 ] ) #if조건절 짝수출력

print()
squares = [x**2 for x in range(1,11)]
print('리스트축약', squares)
squares = list(map(lambda x: x**2, range(1,11)))
print('람다식구현', squares)


"""
리스트축약 [1, 0, 1, 0, 1, 1, 0]
리스트축약 ['ham', 'ham', 'ham']
리스트축약 ['ham', 'ham', 'ham']
리스트축약 [2, 4, 6, 8, 10]

리스트축약 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
람다식구현 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
























print()
print()