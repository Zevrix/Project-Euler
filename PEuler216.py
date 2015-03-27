def miller_rabin(x):
    if x == 1 or x == 2:
        if x == 1:
            return False
        if x == 2:
            return True
    elif x < 2047:
        L1 = [2]
    elif x < 1373653:
        L1 = [2,3]
    elif x < 9080191:
        L1 = [31,73]
    elif x < 25326001:
        L1 = [2,3,5]
    elif x < 4759123141:
        L1 = [2,7,61]
    elif x < 1122004669633:
        L1 = [2,13,23,1662803]
    elif x < 2152302898747:
        L1 = [2,3,5,7,11]
    elif x < 3474749660383:
        L1 = [2,3,5,7,11,13]
    elif x < 341550071728321:
        L1 = [2,3,5,7,11,13,17]
    elif x < 3825123056546413051:
        L1 = [2,3,5,7,11,13,17,19,23]
    d = x-1
    s = 0
    while d % 2 != 1:
        d = d/2
        s = s + 1
    for a in L1:
        L2 = []
        for z in range(s):
            y = pow(a,int(2**z*d),x)
            L2.append(y)
            if y == x - 1 or L2[0] == 1:
                break
        if L2[0] != 1 and x-1 not in L2:
            return False
    return True

from time import time

stime = time()

count = 0

for x in range(2*10**7+1,5*10**7+1):
    if miller_rabin(2*x**2-1) == True:
        count = count + 1

print(count)
print(time()-stime)

#7 1-10
#45 1-10**2
#303 1-10**3
#2202 1-10**4
#17185 1-10**5
#141444 1-10**6
#127231 10**6+1-2*10**6
#932300 2*10**6+1-10**7
#1200975 1-10**7
#1097113 10**7+1-2*10**7
#3139761 2*10**7+1 - 5*10**7

#5437849

