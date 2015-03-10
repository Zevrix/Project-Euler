from Functions import sieve
from time import time
from decimal import *

getcontext().prec = 30000

stime = time()

L1 = sieve(10**7)

L2 = [4]*1+[3]*3+[2]*40+[1]*500407

L3 = []

for x in range(len(L2)):
    L3.append(L1[x]**(2**L2[x]-1))

L4 = []

for x in range(0,len(L3),21):
    prod2 = 1
    for y in range(x,x+21):
        prod2 = Decimal(prod2) * Decimal(L3[y])
    L4.append(prod2%Decimal(500500507))

L5 = []

for x in range(0,len(L4)-1,10):
    prod2 = 1
    for y in range(x,x+10):
        prod2 = Decimal(prod2) * Decimal(L4[y])
    L5.append(prod2%Decimal(500500507))

L5.append(L4[-1])

prod = 1

for x in L5:
    prod = Decimal(prod)*Decimal(x)

print(prod%Decimal(500500507))
