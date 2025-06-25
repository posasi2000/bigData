
kor, eng, total = 90, 85, 0
avg = 0.0
result = '안내문'
grade = 'F' #학점관리 변수 

total = kor + eng 
avg = float(total) / 2

if avg >= 70 :
  result = '결과: 축합격'
else :
  result = '결과: 재시험'
  

if avg >= 90  :
  grade = 'A'
elif avg >= 80 :
  grade = 'B'
elif avg >= 70 :
  grade = 'C'
elif avg >= 60 : 
  grade = 'D'
else:
  grade = 'F'

print(f'총점 = {total}')
print(f'평균 = {avg}')
print(f'학점 = {grade}')

print(f'♣{result}♣')


# 학점출력 
'''
세번째 if ~ elif ~ elif ~  else
 if 조건1 :
      조건1 만족시처리
 elif 조건2 :
      조건2 만족시처리
 elif 조건3 :
      조건3 만족시처리
 else :
      조건불만족처리 
'''
print()