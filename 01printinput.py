# 초간단 연산및 출력, 예외처리 

a, b, gob  = 0, 0, 0

a = 9
b = 3
# 사칙연산 + -  *  /  %
# 문제 9 * 3 = 27 출력 a,b,gob변수 최대한 이용

gob = a * b

print('첫번째 방법')
print(a, '*', b, '=', gob)
print()

b = 4
gob = a * b
print('두번째 방법')
print('%d * %d = %d' %(a, b, gob) )
print()


b = 5
gob = a * b
print('세번째 방법')
print('{} * {} = {}'.format(a, b, gob) )
print()

b = 6
gob = a * b
print('네번째 방법')
print(f'{a} * {b} = {gob}' )
print()


x, y, total, mok = 0,0,0,0

x = int(input('x 정수입력>>> '))  #90 숫자입력
y = int(input('y 정수입력>>> '))  #85 숫자입력
total = x + y
mok = x / y 
print(f'{x} + {y} = {total}')
print(f'{x} / {y} = {mok}')
print(f'{x} / {y} = {round(mok,2)}')
print('%d / %d = %.2f'%(x, y, mok))
print('- ' * 60)


# 문제제시  만약에 숫자대신 문자나, 실수형 입력받으면 에러발생 try~except해결
# x = int(input('x 정수입력>>> '))  #  숫자입력대신 문자, 문자열, 실수형 입력받으면 에러발생
# y = int(input('y 정수입력>>> '))  #  숫자입력대신 문자, 문자열, 실수형 입력받으면 에러발생
# total = x + y
# mok = x / y 
# print(f'{x} + {y} = {total}')
# print(f'{x} / {y} = {mok}')
# print(f'{x} / {y} = {round(mok,2)}')
# print('%d / %d = %.2f'%(x, y, mok))
# print('- ' * 60)
# print()

# 참고 하셔요 
try:
    pass
except:
    pass  



# pip install  numpy  pandas  matplotlib  seaborn  scikit-learn  nltk  # 한번에 다 설치
# pip install opencv-python
# pip list

# OpenCV = Open Source Computer Vision 라이브러리 
# pip install opencv-python 설치
# pip install cv2 노노노 설치하는것 아닙니다

# 쥬피터 !pip install  pandas
# 쥬피터 !pip install  numpy
# 쥬피터 !pip install  scikit-learn 
