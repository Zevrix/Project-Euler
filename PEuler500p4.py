from Functions import sieve
from time import time
from decimal import *

getcontext().prec = 30000

stime = time()

L1 = sieve(10**7)

L2 = [5]*1+[4]*3+[3]*11+[2]*381+[1]*499688

L3 = []

for x in range(len(L2)):
    L3.append(L1[x]**(2**L2[x]-1))

L4 = []

for x in range(0,len(L3),26):
    prod2 = 1
    for y in range(x,x+26):
        prod2 = prod2 * L3[y]
    L4.append(prod2%500500507)

L5 = []

for x in range(0,len(L4),59):
    prod2 = 1
    for y in range(x,x+59):
        prod2 = prod2*L4[y]
    L5.append(prod2%500500507)


prod = 1

for x in L5:
    prod = prod * x

print(prod%500500507)

#35407281 is the answer
