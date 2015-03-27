from time import time
from random import randint
from math import sqrt
from decimal import *

getcontext().prec = 25

stime = time()

x = 1

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            L1 = [1,a,2,b,3,c,4,d,5,e,6,f,7,g,8,2,9,0,0]
                            L2 = [1,a,2,b,3,c,4,d,5,e,6,f,7,g,8,6,9,0,0]
                            n = int(''.join(map(str,L1)))
                            n2 = int(''.join(map(str,L1)))
                            if Decimal(n).sqrt() % 1 == 0:
                                print(n)
                            if Decimal(n2).sqrt() % 1 == 0:
                                print(n2)
    
print(time()-stime)

#im dumb

for num in (a + b for a in (30, 70) for b in range(1389026600, 1010101000, -100)):
	if str(num * num)[::2] == '1234567890':
		print(num)

#above code gives the answer
