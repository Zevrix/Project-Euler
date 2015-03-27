from time import time

stime = time()

from operator import xor

count = 0

for n in range(1,2**30+1):
    if xor(xor(n,2*n),3*n) == 0:
        count = count + 1

print(count)
print()
print(time()-stime)

#2178309
#24 min
#a bit brute-forcy but I knew about the xor so that's something
