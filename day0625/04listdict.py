"""
list [ ] 중복가능,순서있음
tuple ( )  직접값대입불가 
set { } 중복x, 순서x
dict { } 키:value값
"""

data = [ 
  [1,2,3,4] ,
  [5,6,7,8] ,
  [9,10,11,12]
]


#중첩for반복문 출력
for a in range(len(data)):
    for b in range(len(data[a])):
        print(data[a][b], end='\t')
    print()

print()
print()
dt = [ 
   [1, 2, 3, 4] ,
   [5, 6, 89] ,
   [9, 3400] ,
   [7, 8, 9, 10, 11]
]


for a in range(len(dt)):
    for b in range(len(dt[a])):
        print(dt[a][b], end='\t')
    print()


print()
#--------------------------------------------------------------------------
# 리스트의 요소 제거
# pop() : 맨 뒤 요소부터 제거
# pop(위치) : 특정 위치의 요소 제거
# remove(값) : 삭제 대상 값 지정
# del 리스트명[인덱스] : 특정 위치의 요소 제거
# clear() 완전삭제

dt=[7,8,9,10,11,15]
print(dt) 
dt[2:5]=[]  #삭제
print(dt)  #[7, 8, 15] 삭제결과출력

dt=[7,8,9,10,11,15]
del dt[2:] #2번째부터 마지막까지 삭제 
print(dt)  #결과 [7, 8]
print()


print('dt.sort() dt.reverse()출력')
dt=[21,7,55,33,9 ]
print('원본' , dt)
dt.sort()
print('소트' , dt)
dt.reverse()
print('역순' , dt)

dt.remove(33)
print(dt)
dt.clear()  #완전삭제
print(dt)  #결과 [ ]
print()

#---------------------------------------------------------------------------
#튜플tuple
pos =  ('신촌', 37.75148, 126.34136, '시청', 36.73982, 127.92851   )
print(pos)

for i in range(len(pos)):
    print(pos[i], end=' ')

print()

for i,v in enumerate(pos):
    print(i,':', v)

print()
print()

#---------------------------------------------------------------------------
#셋 set 중복허용안함 
wish = {'bc', 2300, 'apple', 2300, 'bc', 79 , 2300, 'apple'}
print(wish)

for b in wish:
    print(b, end='  ')

print()
wish.add('kb')  #set 항목추가 add()
wish.add('bc')  #set 항목추가 add()
wish.add('best')  #set 항목추가 add()
print(wish)
print()

page=list(wish) #리스화해서 접근
for a in page:
    print(a, end='\t')  

print()
print()
#---------------------------------------------------------------------------
#로또중복체크를 set함수로 이동
import random

lotto = set() #lotto = {} 딕션으로인식함
result=True

while result:
    num=random.randint(1,45)
    if len(lotto) >= 6: 
        result=False
    else:
        #lotto.append(num)
        lotto.add(num)

print()
print(lotto)
lotto2=list(lotto) 
lotto2.sort( )
print(lotto2)

for i in range(0,len(lotto2)):
    print(lotto2[i], end="  ")
print()
print()

#---------------------------------------------------------------------------
#딕트=dict
print('dict연습 ')
mysite  = { 1:'네이버', 2:'카카오' } #딕트 dict
print(mysite) #{1: '네이버', 2: '카카오'}

#해결1]   3:파이썬등록
mysite[3] = '파이썬'
print(mysite)

#해결2] 네이버대신 아마존수정
mysite[1] = '아마존'
print(mysite)


#해결3]  2값 카카오 출력만
print(mysite[2])      #[키값]  없으면 실행에러 
print(mysite.get(2))   #get()함수로 접근  없으면 None


#해결4]  3,5값 있는지 체크 in 
print( 5 in mysite ) #False
print( 3 in mysite ) #True
print()
print()


mysite  = { 1:'애플사', 2:'구글사', 3:'ms사'}
for k in mysite:
    print(k, ':', mysite[k])

print()
for i,k in enumerate(mysite):
    print(i,'번째' ,k, ':', mysite[k])
    
print()
for k,v in mysite.items():
    print(k,':', v)







