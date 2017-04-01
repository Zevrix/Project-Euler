from math import factorial
from time import time
from Functions import sieve

memoTable = {}

sTime = time()

upTo = 100

toDo = [0]*(upTo+1)

primes = sieve(upTo)

for x in primes:
    toDo[x] = x

def pfDict(n):
    pDict = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            if d not in pDict:
                pDict[d] = 0
            pDict[d] += 1
            n /= d
        d += 1    
    if n > 1:
        if n not in pDict:
            pDict[int(n)] = 0
        pDict[int(n)] += 1
    return pDict

def findDivSum(a, b):
    k = b
    s = 0
    while k <= a:
        s += a // k
        k = k * b
    return s

def addToMemo(x):
    if x[1] == 1:
        memoTable[x] = x[0]
        return x[0]
    elif x[1] <= x[0]:
        memoTable[x] = x[0]*x[1]
        return x[0]*x[1]
    else:
        n = x[0]*x[1]
        while findDivSum(n, x[0]) >= x[1]:
            n -= x[0]
        memoTable[x] = n + x[0]
        return n + x[0]
    
def findM(l, fDict):
    if toDo[l] == 0:
        if 2*l <= upTo and toDo[2*l] == 0:
            cDict = dict(fDict)
            if 2 not in cDict:
                cDict[2] = 0
            cDict[2] += 1
            findM(2*l, cDict)
            
        if 3*l <= upTo and toDo[3*l] == 0:
            cDict = dict(fDict)
            if 3 not in cDict:
                cDict[3] = 0
            cDict[3] += 1
            findM(3*l, cDict)
            
        if 5*l <= upTo and toDo[5*l] == 0:
            cDict = dict(fDict)
            if 5 not in cDict:
                cDict[5] = 0
            cDict[5] += 1
            findM(5*l, cDict)

        if 7*l <= upTo and toDo[7*l] == 0:
            cDict = dict(fDict)
            if 7 not in cDict:
                cDict[7] = 0
            cDict[7] += 1
            findM(7*l, cDict)
            
        mList = []
        for x in fDict:
            if (x, fDict[x]) in memoTable:
                mList.append(memoTable[(x, fDict[x])])
            else:
                mList.append(addToMemo((x, fDict[x])))
        toDo[l] = max(mList)

n = 0

for l in range(2,upTo+1):
    if l % 10**5 == 0:
        print(l)
    if toDo[l] == 0:
        n += 1
        fDict = pfDict(l)
        findM(l, fDict)

print(n)
print(sum(toDo))
print(time()- sTime)

#64938007616 for 10**6 ~20 sec
#246342393590 for 10**6*2  ~50 sec
