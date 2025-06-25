
# test.py
a,b,ret = 7,4,0 

ret = a * b 
print(a,'*',b,'=',ret)
print('%d * %d = %d' %(a,b,ret))  #%d  %c  %s  %f
print('{} * {} = {}'.format(a,b,ret)) #format함수
print(f'{a} * {b} = {ret}') 
print()


msg=1234
print('|{}|'.format(msg))
print('|{:^10}|'.format(msg))   # ^중앙맞춤
print('|{:>10}|'.format(msg))   # >오른쪽맞춤
print('|{:<10}|'.format(msg))   # <왼쪽맞춤
print()
print('|{:0>10,}|'.format(msg))   #0000001,234출력
print('|{:*>10,}|'.format(msg))   #******1,234출력
print('|{:,}|'.format(1234567))	  #1,234,567  권장 
print()

mok = 34.569
print(mok)
print('%d' %(mok))      #정수값 34
print('%f' %(mok))      #실수값 34.569000
print('%4.2f' %(mok))   #실수값  34.57  
print(round(mok,2))     #내장함수값 34.57  
print()