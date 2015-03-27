from time import time
from math import factorial

stime = time()

L4 = list(range(1,151))

L4.remove(1)
L4.remove(2)
L4.remove(6)
L4.remove(3)
L4.remove(9)
L4.remove(27)
L4.remove(7)
L4.remove(4)
L4.remove(10)
L4.remove(28)
L4.remove(8)
L4.remove(5)
L4.remove(11)
L4.remove(33)
L4.remove(15)
L4.remove(29)
L4.remove(12)
L4.remove(24)
L4.remove(18)

L5 = [13,15,16,19,23,25,26,29,36,39,44,49,67]

LTemp = []

LFinal = [1,2,3,5,6,9]

def fact_dig(x):
    f = 0
    L1 = [int(i) for i in str(x)]
    for i in range(len(L1)):
        f = f + factorial(L1[i])
    L2 = [int(i) for i in str(f)]
    if sum(L2) in L4:
        return(sum(L2))
    return(False)

while True:
    L6 = [int(i) for i in str(L5[0])]
    for j in range(1,10):
        for i in range(len(L5)):
            c = fact_dig(j*10**len(L6)+L5[i])
            if c != False:
                L4.remove(c)
                LTemp.append(j*10**len(L6)+L5[i])
                LFinal.append(j*10**len(L6)+L5[i])
                print(c, j*10**len(L6)+L5[i])
    L5 = LTemp
    LTemp = []

#there's is something wrong but my method/code is sound
#but the actual formula of inserting 1-9 in the first
#decimal point doesn't work all the time
#still .. cool program
