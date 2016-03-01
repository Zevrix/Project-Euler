f = open("peuler89.txt", "r")

lines = f.readlines()

L1 = []
L2 = []
L3 = []

for line in lines:
    L1.append(line)

for x in range(len(L1)-1):
    L1[x] = L1[x][:-1]

totalChar = 0

for x in L1:
    totalChar += len(x)

def romanToInt(num):
    total = 0
    ints = []
    for x in num:
        if x == 'M':
            ints.append(1000)
        if x == 'D':
            ints.append(500)
        if x == 'C':
            ints.append(100)
        if x == 'L':
            ints.append(50)
        if x == 'X':
            ints.append(10)
        if x == 'V':
            ints.append(5)
        if x == 'I':
            ints.append(1)
    k = 0
    while k < len(ints)-1:
        if ints[k] >= ints[k+1]:
            total += ints[k]
        elif ints[k] < ints[k+1]:
            total += ints[k+1]-ints[k]
            k += 1
        k += 1
    if k != len(ints):
        total += ints[-1]
    return total
    
for x in L1:
    L2.append(romanToInt(x))

numKey = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
          10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
          100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
          1000: 'M', 2000: 'MM', 3000: 'MMM', 4000: 'MMMM'}

for x in L2:
    L4 = [int(i) for i in str(x)]
    L4.reverse()
    romNum = ''
    for x in range(len(L4)):
        L4[x] *= 10**x
    L4.reverse()
    for x in L4:
        romNum += numKey[int(x)]
    L3.append(romNum)

totalChar2 = 0

for x in L3:
    totalChar2 += len(x)

print(totalChar-totalChar2)

#743 wooo
