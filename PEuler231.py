from Functions import prime_factors
from time import time

stime = time()

a = 1060148425197
b = 1060148425197
c = 1060148425197

for x in range(4264497,20000001):
    L4 = prime_factors(x)
    for y in L4:
        a = a + y
        if x <= 15000000:
            b = b + y
        if x <= 5000000:
            c = c + y

print(a-b-c)
print(time()-stime)

#7526965179680

#a = 21006412112977
#b = 12038156606683
#c = 1441290326614
