
jumin = '901224' #주민번호 6자릿수 
print(jumin)
# print(jumin + 6812)  #에러 TypeError: can only concatenate str (not "int") to str
print(int(jumin) + 6812) #908036
print(type(jumin)) #<class 'str'>
print(len(jumin))  #6자릿수
print(jumin + str(730)) #901224730 문자열 
print(1200.3456 + float(jumin)) #902424.3456 실수

# 함수는 처리 단위이름 
# print()모니터출력, int()정수화, type()타입, len()길이, str()문자화 , float()실수
# round(데이터,자릿수),  input('안내문')키보드입력