from decimal import *

getcontext().prec = 10000

def fib(n):
    L1 = [1,1]
    while len(L1) != n:
        L1.append(L1[-1]+L1[-2])
    return L1

def p(n):
    L1 = []
    if str(bin(n)).count('1') == 1:
        return []
    L1 = [n]
    while str(bin(L1[-1])).count('1') != 1:
        if L1[-1] % 2 == 0:
            L1.append(int(Decimal(L1[-1])/Decimal(2)))
        else:
            L1.append(int(Decimal(L1[-1])*Decimal(3)+1))
    return L1[:len(L1)-1]

def order(L1):
    L2 = []
    L3 = list(L1)
    L3.sort()
    for x in L1:
        L2.append(L3.index(x)+1)
    return L2

def inv_collatz(n):
    n = int(Decimal((n-1))/Decimal(3))
    L1 = [[n]]
    while len(L1) != 18:
        L2 = list(L1[-1])
        L3 = []
        for x in L2:
            L3.append(int(x*2))
        for y in L2:
            if (Decimal((y-1))/Decimal(3)) % 1 == 0 and (Decimal((y-1))/Decimal(3)) % 2 == 1:
                L3.append(int(Decimal(y-1)/Decimal(3)))
        L1.append(L3)
    return L1[-1]

L4 = []
L5 = []

for n in range(2,10000):
    L1 = inv_collatz(4**n)
    for x in L1:
        if len(p(x)) != 18:
            print(n)
        a = order(p(x))
        if a not in L4:
            L4.append(order(p(x)))
            L5.append(n)
            print(len(L4),p(x),n)

#f(10) = 55 (ended on 4**80)
#f(11) = 89 (ended on 4**122)
#f(12) = 144 (ended on 4**242)
#f(13) = 233 (ended on 4**365)
#f(14) = 377 (ended on 4**728)
#f(15) = 611 (ended on 4**1094) (fibonacci = 610)
#f(16) = 989 (ended on 4**2186) (fibonacci = 987) 
#f(17) = 1600 (ended on 4**3281) (fibonacci = 1597)
