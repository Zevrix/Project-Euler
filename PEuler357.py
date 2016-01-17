from Functions import miller_rabin
from Functions import factors
from Functions import sieve
from Functions import prime_factors
from time import time

stime = time()

L1 = []
LP = sieve(100000)

print(time()-stime)

for x in LP:
    s = x-1
    c = 0
    for k in factors(s):
        n = k+s/k
        if miller_rabin(int(n)):
            c += 1
    if c == len(factors(s)):
        L1.append(s)

L2 = []

for x in range(len(L1)-1):
    L2.append(L1[x+1]-L1[x])

print(time()-stime)

twinP = []

for x in range(len(LP)-1):
    if LP[x+1]-LP[x] == 2:
        twinP.append(LP[x])

#if n is in L1 then n+1 is prime
#numbers of this type imply that if a*b = n then a+b is prime
