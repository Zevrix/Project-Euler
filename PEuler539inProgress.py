from collections import Counter
from time import time

stime = time()

def oddElim(L1):
    n = 1
    if len(L1) == 1:
        return L1[0]
    while len(L1) > 1:
        if n == 1:
            L1[0:len(L1):2] = [0]*len(range(0,len(L1),2))
            L1 = list(filter(None, L1))
            n *= -1
        elif n == -1:
            L1[-1:-(len(L1)+1):-2] = [0]*len(range(-1,-(len(L1)+1),-2))
            L1 = list(filter(None, L1))
            n *= -1
    return(L1[0])
    
L2 = []
        
for x in range(1,1001):
    L1 = [k for k in range(1,x+1)]
    L2.append(oddElim(L1))

L3 = list(set(L2))
L3.sort()

L4 = {}

for x in L3:
    L4[x] = 0

for x in L2:
    L4[x] += 1
    
print(time()-stime)

#for x in sorted(L4):
#    print(x,L4[x])

print(sum(L2))
