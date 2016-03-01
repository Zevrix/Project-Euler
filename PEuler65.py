from fractions import gcd

L1 = [2]

x = 2

while len(L1) != 100:
    L1.append(1)
    L1.append(x)
    L1.append(1)
    x += 2

def reduce(n,d):
    while gcd(n,d) != 1:
        n /= gcd(n,d)
        d /= gcd(n,d)
    return [n,d]

def addFrac(a,b,c,d):
    n = a*d+c*b
    d = b*d
    return reduce(n,d)

def divideOne(L1):
    return [L1[1],L1[0]]

for x in range(len(L1)):
    L1[x] = [L1[x],1]

k = L1[-1]

for x in range(len(L1)-2,-1,-1):
    k = divideOne(k)
    k = addFrac(L1[x][0],L1[x][1],k[0],k[1])
    
L2 = [int(i) for i in str(k[0])]

print(sum(L2))

#272, 125 problems solved, top 0.91%, we made it
