from time import time

stime = time()

def prime_factors(n):
    L1 = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            L1.append(int(d))
            n = n/d
        d = d + 1
    if n > 1:
        L1.append(int(n))
    return L1

def resilience(L2, LCheck):
    L2[0] = 0
    L2[1] = 0
    for x in LCheck:
        L2[x:len(L2):x] = [0] *len(range(x,len(L2),x))
    L2[1] = 1
    return list(filter(None,L2))


count = 0

L3 = []

for x in range(2,12001):
    if x % 1000 == 0:
        print(x," done.")
    LCheck = list(set(prime_factors(x)))
    L1 = [x for x in range(x)]
    L2 = resilience(L1,LCheck)
    for y in L2:
        if y/x < 1/2 and y/x > 1/3:
            count += 1

print()
print(time()-stime)
print()
print(count)

#7295372 o bby
