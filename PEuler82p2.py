f = open("PEuler82Matrix.txt", "r")

L1 = []

lines = f.readlines()

for line in lines:
    lineList = line.split(',')
    lineList[-1] = lineList[-1][:-1]
    for x in range(len(lineList)):
        lineList[x] = int(lineList[x])
    L1.append(lineList)

"""L1 = [[131,673,234,103,18],
      [201,96,342,965,150],
      [630,803,746,422,111],
      [537,699,497,121,956],
      [805,732,524,37,331]]"""

L2 = [] #holds diamond array structure for L1

def printMat(L1):
    """Prints the matrix so that it is somewhat readable."""
    for x in L1:
        for y in x:
            print(str(y) + (6 - len(str(y))) * ' ', end='')
        print()
        print()
    print("""

    """)
    
def diamondArray(L2):
    """Turns inputted n by n 2D array into an equivalent diamond-shaped array."""
    k = 0
    n = 0

    while len(L2) != len(L1):
        L3 = []
        n = k
        while n != -1:
            L3.append(L1[n][k-n])
            n -= 1
        L2.append(L3)
        k += 1

    k = len(L1)-1
    n = 1

    while len(L2) != len(L1)*2-1:
        L3 = []
        p = 0
        while n+p <= k:
            L3.append(L1[k-p][n+p])
            p += 1
        L2.append(L3)
        n += 1

diamondArray(L2)

"""LSol = []

for x in range(0,len(L1)):
    LSol.append(L1[x][len(L1)-1])

print(LSol)
print()

for x in range(len(L1)-2, -1, -1):
    LSol[0] += L1[0][x]
    for y in range(1,len(L1)):
        LSol[y] = min(LSol[y-1]+L1[y][x],LSol[y]+ L1[y][x])
    for y in range(len(L1)-2, -1, -1):
        LSol[y] = min(LSol[y],LSol[y+1] +L1[y][x])
    print(LSol)"""


LCop = []
for x in L1:
    LCop.append(list(x))


for x in range(len(LCop)-1,0,-1):
    LVert1 = [LCop[k][x] for k in range(len(LCop))]
    LVert2 = [LCop[k][x-1] for k in range(len(LCop))]
    LVert2[0] += LVert1[0]
    for y in range(1,len(LCop)):
        LVert2[y] = min(LVert2[y-1]+LVert2[y],LCop[y][x]+LVert2[y])
    for y in range(len(LCop)-2,-1,-1):
        LVert2[y] = min(LVert2[y],LVert2[y+1]+LCop[y][x-1])
    for y in range(len(LCop)):
        LCop[y].remove(LCop[y][x])
    for y in range(len(LCop)):
        LCop[y][x-1] = LVert2[y]


print(min(LCop))
