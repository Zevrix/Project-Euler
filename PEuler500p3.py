from Functions import sieve
from time import time

stime = time()

L1 = sieve(10**7)

print(time()-stime)

L2 = [0]*len(L1)

n = 500500

#this works fine but still slow, about 10 seconds per thousand that increases
#odd early lag into fast speed up, then gradual slow down
#the lag is until all the numbers in L3 are present in L2 because then it stops having to cycle through the entire list
#the gradual slow down comes from the increasing index of the first 0 resulting in deeper searches

while n != 0:
    L3 = [4,3,2,1,0]
    L4 = []
    for x in L3:
        if x in L2:
            k = L2.index(x)
            if x != 0:
                L4.append((L1[k]**(2**(L2[k]+1)-1))-(L1[k]**(2**L2[k]-1)))
            else:
                L4.append(L1[k])
        else:
            L4.append(10**7)
    a = L2.index(L3[L4.index(min(L4))])
    L2[a] = L2[a] + 1
    n = n - 1
    if n % 1000 == 0:
        print(n,time()-stime)
    
