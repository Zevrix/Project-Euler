def sieve(n):
    L1 = list(range(n+1))
    L1[1] = 0
    limit = int(round(n**0.5))
    for i in range(2, limit + 1): 
        if L1[i]:
            L1[i*i: n+1: i] = [0] * len(range(i*i, n+1, i))
    return list(filter(None,L1))

L1 = sieve(1000)
L2 = [2]
L3 = [2]

def prime_connections(L6):
    L5 = []
    for h in range(len(L6)):
        if len(str(L6[h])) < 3:
            for x in range(1,10):
                L4 = [int(i) for i in str(L6[h])] 
                L4.insert(0,x)
                y = int(''.join(map(str,L4)))
                if y in L1 and y not in L6 and y not in L3:
                    L5.append(y)
            for z in range(1,10):
                L4 = [int(i) for i in str(L6[h])]
                L4.append(z)
                a = int(''.join(map(str,L4)))
                if a in L1 and a not in L6 and a not in L3:
                    L5.append(a)

        for b in range(len(str(L6[h]))):
            L4 = [int(i) for i in str(L6[h])]
            for c in range(10):
                L4[b] = c
                d = int(''.join(map(str,L4)))
                if d in L1 and d not in L6 and d not in L3:
                    L5.append(d)
    return list(set(L5))


while len(L2) != 0:
    L7 = prime_connections(L2)
    for e in range(len(L7)):
        L3.append(L7[e])
    L2 = L7
    
#I'm an idiot, no prime in the chain can exceed the prime we are trying to reach
#maybe i can use this but im done for now
            
                
    
