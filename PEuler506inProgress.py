L1 = [1,2,3,4,3,2]
L2 = L1 * 50000
L3 = []

for x in range(1,12):
    y = 1
    while y != (len(L2)-1) and len(L3) != x:
        if sum(L2[:y]) == x:
            L3.append(L2[:y])
            print(L2[:y])
            L2 = L2[y:]
        y = y + 1

total = 0

for x in L3:
    n = int(''.join(map(str,x)))
    total = total + n

print(total%123454321)
