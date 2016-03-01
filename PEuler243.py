from time import time

stime = time()

def sieve(n):
    L1 = list(range(n+1))
    L1[1] = 0
    limit = int(round(n**0.5))
    for i in range(2, limit + 1): 
        if L1[i]:
            L1[i*i: n+1: i] = [0] * len(range(i*i, n+1, i))
    return list(filter(None,L1))

L1 = sieve(1000)
LCheck = L1[:9]

prod = 1

for x in LCheck:
    prod *= x

print(prod)
print()

L2 = [1]*prod

def resilience(L2, LCheck):
    L2[0] = 0
    L2[1] = 0
    for x in LCheck:
        L2[x:len(L2):x] = [0] *len(range(x,len(L2),x))
    return list(filter(None,L2))


L3 = resilience(L2,LCheck)
print(time()-stime)
print()
print(len(L3))
k = 15499/94744
print()
print(k)
print((len(L3)+1)/(prod-1))
