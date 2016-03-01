cache = [0]*300

def blockComb(m,n):
    sol = 1
    if n > m:
        return sol
    if cache[m] != 0:
        return cache[m]
    for x in range(0, m-n+1):
        for y in range(n, m-x+1):
            sol += blockComb(m - x - y - 1, n)
    cache[m] = sol
    return sol

print(blockComb(50,3))

for x in range(150,180):
    cache = [0]*300
    if blockComb(x,50) > 10**6:
        print(x, blockComb(x,50))
        break

#answer to 114: blockComb(50,3) = 16475640049
#answer to 115: blockComb(168,50) = 1053389 so 168 is the answer
