import pandas as pd

fname = './data/emp.csv'  #성공 encoding='euc-kr'  성공encoding='cp949'
emp = pd.read_csv(fname, encoding='euc-kr')
print(emp)
print('- ' * 30)

print()
print(emp['Name'])  #Name열필드추출, name기술하면에러, 필드의 대소문자구별
print('- ' * 30)

print() 
print(emp.loc[3])   # emp.loc(3)  접근하면 에러발생 까사노씨 정보출력
print()

print(emp.loc[2:5])  # loc[시작:5], iloc[시작:끝-1]
print('- ' * 30)
print()

print("2시작행:5끝행 , '이름열':'급여열'")
print(emp.loc[2:5 , 'Name':'Pay'])  # loc[2시작:5 , '시작열':'끝열']
print()

print(emp.loc[: , 'Name':'Pay'])   # loc[ : , '시작열':'끝열'] #모든행
print()





print()