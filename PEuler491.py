from itertools import combinations
from math import factorial

L1 = list(combinations([0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9],10))

L1 = list(set(L1))

L2 = []

for x in range(len(L1)):
    if (sum(L1[x])-(90-sum(L1[x]))) % 11 == 0:
        L2.append(L1[x])

total = 0


for y in range(len(L2)):
    a = L2[y].count(0)
    b = L2[y].count(1)
    c = L2[y].count(2)
    d = L2[y].count(3)
    e = L2[y].count(4)
    f = L2[y].count(5)
    g = L2[y].count(6)
    h = L2[y].count(7)
    i = L2[y].count(8)
    j = L2[y].count(9)

    n = 0
    o = 0

    if a == 2:
        n = n + 1
    if b == 2:
        n = n + 1
    if c == 2:
        n = n + 1
    if d == 2:
        n = n + 1
    if e == 2:
        n = n + 1
    if f == 2:
        n = n + 1
    if g == 2:
        n = n + 1
    if h == 2:
        n = n + 1
    if i == 2:
        n = n + 1
    if j == 2:
        n = n + 1

    if a == 0:
        o = o + 1
    if b == 0:
        o = o + 1
    if c == 0:
        o = o + 1
    if d == 0:
        o = o + 1
    if e == 0:
        o = o + 1
    if f == 0:
        o = o + 1
    if g == 0:
        o = o + 1
    if h == 0:
        o = o + 1
    if i == 0:
        o = o + 1
    if j == 0:
        o = o + 1
        
    if a == 0:
        pos = factorial(10)/factorial(2)**n
        neg = factorial(10)/factorial(2)**o
        total = total + pos*neg

    elif a == 1:
        pos = 9 * factorial(9)/factorial(2)**n
        neg = factorial(10)/factorial(2)**o
        total = total + pos*neg

    elif a == 2:
        pos = 8 * factorial(9)/factorial(2)**n
        neg = factorial(10)/factorial(2)**o
        total = total + pos*neg

print(total)
