f = open("PEuler83.txt", "r")

L1 = []

lines = f.readlines()

for line in lines:
    lineList = line.split(',')
    lineList[-1] = lineList[-1][:-1]
    for x in range(len(lineList)):
        lineList[x] = int(lineList[x])
    L1.append(lineList)

L1 = [[131,673,234,103,18],
      [201,96,342,965,150],
      [630,803,746,422,111],
      [537,699,497,121,956],
      [805,732,524,37,331]]

def printMat(L1):
    """Prints the matrix so that it is somewhat readable."""
    for x in L1:
        for y in x:
            print(str(y) + (6 - len(str(y))) * ' ', end='')
        print()
        print()
    print("""

    """)

L2 = [] #will contain layer matrix

def layerMatrix(L2):
    k = len(L1)-1
    for n in range(len(L1)-1,-1,-1):
        L3 = []
        t = k
        while t != n:
            L3.append(L1[t][n])
            t -= 1
        for p in range(t,len(L1)):
            L3.append(L1[t][p])
        L2.append(L3)

def nextTo(LCop,x,y):
    if y < x:
        return LCop[x-1][y]
    if y > x:
        return LCop[x-1][y-2]
        
    

layerMatrix(L2)

LCop = []

for x in L2:
    LCop.append(list(x))


for x in range(len(LCop)-1):
    LCop[x+1][0] += LCop[x][0]
    for y in range(1,len(LCop[x+1])):
        if y == x+1:
            LCop[x+1][y] += LCop[x+1][y-1]
        else:
            LCop[x+1][y] += min(LCop[x+1][y-1], nextTo(LCop,x+1,y))
    for y in range(len(LCop[x+1])-2,-1,-1):
        LCop[x+1][y] = min(LCop[x+1][y],L2[x+1][y]+LCop[x+1][y+1])
    printMat(LCop)
            
    

