L1 = ['x','y','z']

L2 = []

L3 = []

count = 0

for a in L1:
    for b in L1:
        for c in L1:
            for d in L1:
                for e in L1:
                    for f in L1:
                        L2.append([a,b,c,d,e,f])

for x in range(len(L2)):
    L3.append([L2[x][:3],L2[x][1:4],L2[x][2:5],L2[x][3:]])

for y in range(len(L3)):
    if ['x','y','z'] in L3[y] or ['x','z','y'] in L3[y] or ['y','x','z'] in L3[y] or ['y','z','x'] in L3[y] or ['z','y','x'] in L3[y] or ['z','x','y'] in L3[y]:
        L3[y] = 0
        count = count + 1

L3 = list(filter(None,L3))

L4 = []
L5 = []
L6 = []
L7 = []

for z in range(len(L3)):
    L4.append(L3[z][0])
    L5.append(L3[z][1])
    L6.append(L3[z][2])
    L7.append(L3[z][3])

#just running tests
