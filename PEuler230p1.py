a = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
b = 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196

x = 'A'
y = 'B'

n = 12

def first_fib(x):
    a = 1
    b = 1
    while True:
        c = a+b
        a = b
        b = c
        if c >= x:
            return c-x+1

from math import ceil

while len(y) < first_fib(ceil((127+19*n)*7**n/100)):
    z = x+y
    x = y
    y = z

c = y[-first_fib(ceil((127+19*n)*7**n/100))]


if c == 'A':
    print(c, int(str(a)[((127+19*n)*7**n)%100-1])*10**n,((127+19*n)*7**n)%100)
else:
    print(c, int(str(b)[((127+19*n)*7**n)%100-1])*10**n,((127+19*n)*7**n)%100)  


#n=0 B 6 27
#n=1 B 90 22 
#n=2 B 200 85
#n=3 A 9000 12
#n=4 B 10000 3
#n=5 B 100000 54
#n=6 A 3000000 9
#n=7 B 90000000 80
#n=8 B 500000000 79
#n=9 B 2000000000 86
#n=10 B 50000000000 33
#n=11 B 100000000000 48


#n=14 A/B 400000000000000 57

#n=16 A/B 50000000000000000 31
