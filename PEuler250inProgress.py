from time import time
from math import factorial
from decimal import *

getcontext().prec = 50

def choose(n,r):
    return (factorial(n))//(factorial(r)*factorial(n-r))

stime = time()

x = 1
c = 0

while x != 250251:
    if x % 5 == 0 and x % 2 == 0:
        c = c + 1
    x = x + 1

#25025 of the numbers below 250251 in the form x ** x are divisible
#by 250 ... non empty sum subset stuff is more complex
#still ... this was pretty clever

print(c)
print(time()-stime)

s = 0
x = 2

while x != 25025:
    s = s + choose(25025,x)
    x = x + 1

print()
print(s)
print(time()-stime)

#this will work ... but take a while
#it didnt work ... but atleast i can form subsets
#ill be back
