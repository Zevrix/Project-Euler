rows = int(input('How many rows? ', ))

from math import floor

def getexp(rows):
    for n in range(1,20):
        if 7**n <= rows <= 7**(n+1):
            return n

exp = getexp(rows)

count = 0

L1 = []

while exp != -1:
    x = floor(rows/(7**exp))
    a = (x*(x+1)/2) * 28**exp
    for i in range(len(L1)):
        a = a * L1[i]
    count = count + a
    print((x*(x+1)/2) * 28**exp, rows, exp, x)
    rows = rows - x*7**exp
    exp = exp - 1
    L1.append(x+1)
    
#2129970655314432 values in the first billion rows of pascals triangle are not divisible by 7

print()
print(count)
