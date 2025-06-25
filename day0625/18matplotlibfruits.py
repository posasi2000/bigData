
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)


fruits = ['apple', 'blue', 'cherry', 'mango']
price = [ 65, 138, 72, 96 ] #갯수,가격

# 해결1] bar, line 가격숫자 표시 
plt.figure(figsize=(14,7))
plt.bar(fruits, price)
plt.plot(fruits, price, color='r', marker='o' , markersize=10)
# 비권장 plt.scatter(fruits, price, color='orange')
plt.title('농수산 과일 가격 수량')
plt.xlabel('과일이름')
plt.ylabel('수량 금액')
plt.grid(axis='y', linestyle='--', alpha=0.6)  # plt.grid(True)


for i in range(len(fruits)):
    value = price[i]
    plt.text( fruits[i], value+0.9, value, fontsize=14,  color='blue',  
                ha='center',  #ha
                va='bottom'   #va
    )

plt.savefig('./images/fruits.png')
print('./images/fruits.png 그래프 저장 성공했습니다 ')
plt.show()


# area = ['서울', '안양', '수원', '일산']
# su1 = [21, 34, 45, 13]
# su2 = [45, 19, 31, 50]
# su3 = [33, 56, 27, 41]
# su4 = [77, 26, 65, 29]









print()
print()
