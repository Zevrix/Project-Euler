from time import time

stime = time()

L1 = []

for x in range(40):
    for y in range(26):
        for z in range(18):
            L1.append(2**x*3**y*5**z)

L1.sort()

L1 = L1[:3429]

def prime_factors(n):
    L1 = []
    d = 2
    while d*d <= n:
        while (n%d) == 0:
            L1.append(d)
            n = n/d
        d = d + 1
    if n > 1:
        L1.append(n)
    L2 = list(set(L1))
    L2[-1] = int(L2[-1])
    return [L1,L2]

def totient(n):
    prod = n
    L1 = prime_factors(n)[1]
    for x in L1:
        prod = prod * (1-1/x)
    return prod


total = 1
count = 1



for x in range(2,100001):
    if int(totient(x)) in L1:
        total = total + x
        count = count + 1

print(total)
print()
print(time()-stime)
