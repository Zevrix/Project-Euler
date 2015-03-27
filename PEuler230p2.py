from math import ceil
from time import time

stime = time()

def fib(x):
    L1 = [1,1]
    a = 1
    b = 1
    while True:
        n = a + b
        a = b
        b = n
        L1.append(b)
        if b > x:
            break
    return L1

L2 = [6]

pi1 = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
pi2 = 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196

for n in range(1,18):
    c = (127+19*n)*7**n
    a = ceil(c/100)
    L1 = fib(a)
    while len(L1) > 2:
        if a > L1[-3]:
            a = a - L1[-3]
            L1 = L1[:-1]
        else:
            L1 = L1[:-2]
    if len(L1) == 1:
        L2.append(str(pi1)[c%100-1])
    else:
        L2.append(str(pi2)[c%100-1])

#sick job d00d 

L2.reverse()
z = int(''.join(map(str,L2)))
print(z)
print(time()-stime)

#850481152593119296
