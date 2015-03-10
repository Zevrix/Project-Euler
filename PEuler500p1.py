from Functions import sieve
from time import time

stime = time()

L1 = sieve(10**7)

print(time()-stime)

L2 = len(L1)*[0]

n = 500500

while n != 0:
    end = 0
    x = 0
    while end != 1:
        k = L2.index(0)
        if x == 0:
            if (L1[x]**(2**(L2[x]+1)-1)-L1[x]**(2**L2[x]-1)) < (L1[x+1]**(2**(L2[x+1]+1)-1)-L1[x+1]**(2**L2[x+1]-1)) and (L1[x]**(2**(L2[x]+1)-1)-L1[x]**(2**L2[x]-1)) < L1[k]:
                L2[x] = L2[x] + 1
                n = n - 1
                end = 1
            else:
                x = x + 1
        else:
            if (L1[x]**(2**(L2[x]+1)-1)-L1[x]**(2**L2[x]-1)) < (L1[x+1]**(2**(L2[x+1]+1)-1)-L1[x+1]**(2**L2[x+1]-1)) and (L1[x]**(2**(L2[x]+1)-1)-L1[x]**(2**L2[x]-1)) < (L1[x-1]**(2**(L2[x-1]+1)-1)-L1[x-1]**(2**L2[x-1]-1)) and (L1[x]**(2**(L2[x]+1)-1)-L1[x]**(2**L2[x]-1)) < L1[k]:
                L2[x] = L2[x] + 1
                n = n - 1
                end = 1
            else:
                x = x + 1
        if x == k:
            L2[k] = L2[k] + 1
            n = n - 1
            end = 1
        if L2[x] == 1 and L2[x-1] == 1 and L2[x+1] == 1:
            L2[k] = L2[k] + 1
            n = n -1
            end = 1
        if L2[x] == L2[x-1] and L2[x] == L2[x+1]:
            x = L2.index(L2[x]-1)
    if n % 1000 == 0:
        print(n,time()-stime)

print(L2[:35])
L5.append(7)

L3 = [x for x in range(1,1001)]
L3.reverse()

L4 = []

for x in range(1000):
    L4.append(pow(L1[x],pow(2,L3[x])-1,500500507))

prod = 1

for y in L4:
    prod = prod*y

print(prod%500500507)
