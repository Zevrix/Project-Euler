from time import time

from decimal import *

stime = time()

L1 = []

for a in range(1,3):
    L1.append([a])

L2 = []

for a in range(1,3):
    for b in range(3):
        L2.append([a,b])

L3 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            L3.append([a,b,c])

L4 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                L4.append([a,b,c,d])

L5 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    L5.append([a,b,c,d,e])

L6 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        L6.append([a,b,c,d,e,f])

L7 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            L7.append([a,b,c,d,e,f,g])

L8 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                L8.append([a,b,c,d,e,f,g,h])

L9 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                for i in range(3):
                                    L9.append([a,b,c,d,e,f,g,h,i])

L10 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                for i in range(3):
                                    for j in range(3):
                                        L10.append([a,b,c,d,e,f,g,h,i,j])

L11 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                for i in range(3):
                                    for j in range(3):
                                        for k in range(3):
                                            L11.append([a,b,c,d,e,f,g,h,i,j,k])

L12 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                for i in range(3):
                                    for j in range(3):
                                        for k in range(3):
                                            for l in range(3):
                                                L12.append([a,b,c,d,e,f,g,h,i,j,k,l])

L13 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                for i in range(3):
                                    for j in range(3):
                                        for k in range(3):
                                            for l in range(3):
                                                for m in range(3):
                                                    L13.append([a,b,c,d,e,f,g,h,i,j,k,l,m])

L14 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                for i in range(3):
                                    for j in range(3):
                                        for k in range(3):
                                            for l in range(3):
                                                for m in range(3):
                                                    for n in range(3):
                                                        L14.append([a,b,c,d,e,f,g,h,i,j,k,l,m,n])

print('Done 14')
print(time()-stime)
print()

L15 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                for i in range(3):
                                    for j in range(3):
                                        for k in range(3):
                                            for l in range(3):
                                                for m in range(3):
                                                    for n in range(3):
                                                        for o in range(3):
                                                            if sum([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]) % 9 == 0:
                                                                L15.append([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o])

print('Done 15')
print(time()-stime)
print()

L16 = []

for a in range(1,3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                for i in range(3):
                                    for j in range(3):
                                        for k in range(3):
                                            for l in range(3):
                                                for m in range(3):
                                                    for n in range(3):
                                                        for o in range(3):
                                                            for p in range(3):
                                                                if sum([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]) % 9 == 0:
                                                                    L16.append([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p])

L17 = []

print('Done 16')
print(time()-stime)
print()
               
LM = []
LKeep = []

#314548450057 = sum of LM 1-10000 - 4995 and 9990 and 9999
#222667111556 for 4995
#111333555778 for 9990
#1111333355557778 for 9999 
#1111981904675169 is the total


for x in range(1,10001):
    y = 1
    check = 0
    if y == 1 and check == 0:
        for a1 in range(len(L1)):
            n = int(''.join(map(str,L1[a1])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 2
    if y == 2 and check == 0:
        for a2 in range(len(L2)):
            n = int(''.join(map(str,L2[a2])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 3
    if y == 3 and check == 0:
        for a3 in range(len(L3)):
            n = int(''.join(map(str,L3[a3])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 4
    if y == 4 and check == 0:
        for a4 in range(len(L4)):
            n = int(''.join(map(str,L4[a4])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 5
    if y == 5 and check == 0:
        for a5 in range(len(L5)):
            n = int(''.join(map(str,L5[a5])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 6
    if y == 6 and check == 0:
        for a6 in range(len(L6)):
            n = int(''.join(map(str,L6[a6])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 7
    if y == 7 and check == 0:
        for a7 in range(len(L7)):
            n = int(''.join(map(str,L7[a7])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 8
    if y == 8 and check == 0:
        for a8 in range(len(L8)):
            n = int(''.join(map(str,L8[a8])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 9
    if y == 9 and check == 0:
        for a9 in range(len(L9)):
            n = int(''.join(map(str,L9[a9])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 10
    if y == 10 and check == 0:
        for a10 in range(len(L10)):
            n = int(''.join(map(str,L10[a10])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 11
    if y == 11 and check == 0:
        for a11 in range(len(L11)):
            n = int(''.join(map(str,L11[a11])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 12
    if y == 12 and check == 0:
        for a12 in range(len(L12)):
            n = int(''.join(map(str,L12[a12])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 13
    if y == 13 and check == 0:
        for a13 in range(len(L13)):
            n = int(''.join(map(str,L13[a13])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 14
    if y == 14 and check == 0:
        for a14 in range(len(L14)):
            n = int(''.join(map(str,L14[a14])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 15
    if y == 15 and check == 0:
        for a15 in range(len(L15)):
            n = int(''.join(map(str,L15[a15])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 16
    if y == 16 and check == 0:
        for a16 in range(len(L16)):
            n = int(''.join(map(str,L16[a16])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 17
    if y == 17 and check == 0:
        for a17 in range(len(L17)):
            n = int(''.join(map(str,L17[a17])))
            if n%x == 0:
                LM.append(Decimal(n)/Decimal(x))
                print(x,n,n/x)
                LKeep.append([x,n,n/x])
                check = 1
                break
        y = 18
        
print()
print(time()-stime)
