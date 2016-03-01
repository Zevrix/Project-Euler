from math import floor
from fractions import gcd
from time import time

stime = time()

L1 = []

for x in range(3,10**6+1):
    if x % 25000 == 0:
        print(x,"done.")
    n = floor(x*3/7)
    while gcd(n,x) != 1:
        n -= 1
    L1.append([n,x])

L1.remove([3,7])

L2 = []

for x in L1:
    L2.append(x[0]/x[1])

print()
print(time()-stime)
print()
print(L1[L2.index(max(L2))])

#428570/999997 ... o boy
