from decimal import *

getcontext().prec = 10

def factors(n):
    L1 = []
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            if (i != n/i):
                L1.append(i)
                L1.append(n/i)
            else:
                L1.append(i)
    L1.sort()
    return L1

for x in range(1,1000000):
    L1 = factors(x)
    total = 0
    for y in range(len(L1)):
        total = total + L1[y]**2
    if len(str(Decimal(total).sqrt())) != 11:
        print(x,total,int(Decimal(total).sqrt()))

#too slow
#but the sqrt check method is actually nice
