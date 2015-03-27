from time import time
from math import floor
from math import factorial

stime = time()

x = 63

L2 = []

while x != 151:
    L1 = [int(floor(x/9)*"9")+(x%9)*10**floor(x/9)]
    i = 0
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
    L2.append(i*1+h*2+g*3+f*4+e*5+d*6+c*7+b*8+a*9)
    x = x + 1
