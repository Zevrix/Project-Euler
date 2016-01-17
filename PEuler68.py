from itertools import permutations
from time import time

stime = time()

L1 = list(permutations([1,2,3,4,5,6,7,8,9,10],10))

print(time()-stime)

L2 = []
L3 = []
L4 = []
L5 = []

for x in L1:
    a = [x[0],x[1],x[2]]
    b = [x[3],x[2],x[4]]
    if sum(b) == sum(a):
        c = [x[5],x[4],x[6]]
        if sum(c) == sum(a):
            d = [x[7],x[6],x[8]]
            if sum(d) == sum(a):
                e = [x[9],x[8],x[1]]
                if sum(e) == sum(a):
                    L2.append(x)

print(time()-stime)

for x in L2:
    a = [x[0],x[1],x[2]]
    b = [x[3],x[2],x[4]]
    c = [x[5],x[4],x[6]]
    d = [x[7],x[6],x[8]]
    e = [x[9],x[8],x[1]]
    lowestExternalNode = min([x[0],x[3],x[5],x[7],x[9]])
    if lowestExternalNode == x[0]:
        L3.append(a+b+c+d+e)
    if lowestExternalNode == x[3]:
        L3.append(b+c+d+e+a)
    if lowestExternalNode == x[5]:
        L3.append(c+d+e+a+b)
    if lowestExternalNode == x[7]:
        L3.append(d+e+a+b+c)
    if lowestExternalNode == x[9]:
        L3.append(e+a+b+c+d)

print(time()-stime)

for x in L3:
    L4.append(int(''.join(str(i) for i in x)))

for x in L4:
    if len(str(x)) == 16:
        L5.append(x)
        
print(time()-stime)
print(max(L5))

#6531031914842725, brute force worked, 13 seconds
