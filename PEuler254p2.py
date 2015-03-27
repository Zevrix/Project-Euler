from math import floor
from time import time
from math import factorial

stime = time()

x = 59

y = 1

L1 = [199999999999]

while y != 1:
    L2 = [int(i) for i in str(y)]
    if sum(L2) == x:
        L1.append(y)
    y = y + 1

print(time()-stime)

L3 = []

for i in range(len(L1)):
    a = floor(L1[i]/factorial(9))
    L1[i] = L1[i] - a * factorial(9)
    b = floor(L1[i]/factorial(8))
    L1[i] = L1[i] - b * factorial(8)
    c = floor(L1[i]/factorial(7))
    L1[i] = L1[i] - c * factorial(7)
    d = floor(L1[i]/factorial(6))
    L1[i] = L1[i] - d * factorial(6)
    e = floor(L1[i]/factorial(5))
    L1[i] = L1[i] - e * factorial(5)
    f = floor(L1[i]/factorial(4))
    L1[i] = L1[i] - f * factorial(4)
    g = floor(L1[i]/factorial(3))
    L1[i] = L1[i] - g * factorial(3)
    h = floor(L1[i]/factorial(2))
    L1[i] = L1[i] - h * factorial(2)
    i = floor(L1[i]/factorial(1))
    L3.append([a+b+c+d+e+f+g+h+i, int(i*"1"+h*"2"+g*"3"+f*"4"+e*"5"+d*"6"+c*"7"+b*"8"+a*"9"),i*1+h*2+g*3+f*4+e*5+d*6+c*7+b*8+a*9])
    
L3.sort()

