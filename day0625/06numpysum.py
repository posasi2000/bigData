import numpy as np
import math

print('제곱근' , math.sqrt(81))
print('제곱근' , np.sqrt(81))  
print('제곱근' , np.emath.sqrt(81))
print()

a = np.arange(1,11)
print(a) #[ 1  2  3  4  5  6  7  8  9 10]
print('합계', sum(a)) #55
print('합계', np.sum(a))  #55  
print('합계', np.add.reduce(a))  #55
print()

a = np.arange(1,11,1)
print(a) #[ 1  2  3  4  5  6  7  8  9 10]

b = np.arange(10,0,-1)  #range(10,0,-1)
print(b) #[10  9  8  7  6  5  4  3  2  1]
print()


