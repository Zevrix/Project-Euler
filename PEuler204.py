def hamming(limit):
    hamming = [1] * limit
    x2, x3, x5, x7, x11, x13, x17, x19, x23, x29, x31, x37, x41, x43, x47, x53, x59, x61, x67, x71, x73, x79, x83, x89, x97 = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=0
 
    for rp in range(1, limit):
        hamming[rp] = min(x2, x3, x5, x7, x11, x13, x17, x19, x23, x29, x31, x37, x41, x43, x47, x53, x59, x61, x67, x71, x73, x79, x83, x89, x97)
        if x2 == hamming[rp]:
            a += 1
            x2 = 2 * hamming[a]
        if x3 == hamming[rp]:
            b += 1
            x3 = 3 * hamming[b]
        if x5 == hamming[rp]:
            c += 1
            x5 = 5 * hamming[c]
        if x7 == hamming[rp]:
            d += 1
            x7 = 7 * hamming[d]
        if x11 == hamming[rp]:
            e += 1
            x11 = 11 * hamming[e]
        if x13 == hamming[rp]:
            f += 1
            x13 = 13 * hamming[f]
        if x17 == hamming[rp]:
            g += 1
            x17 = 17 * hamming[g]
        if x19 == hamming[rp]:
            h += 1
            x19 = 19 * hamming[h]
        if x23 == hamming[rp]:
            i += 1
            x23 = 23 * hamming[i]
        if x29 == hamming[rp]:
            j += 1
            x29 = 29 * hamming[j]
        if x31 == hamming[rp]:
            k += 1
            x31 = 31 * hamming[k]
        if x37 == hamming[rp]:
            l += 1
            x37 = 37 * hamming[l]
        if x41 == hamming[rp]:
            m += 1
            x41 = 41 * hamming[m]
        if x43 == hamming[rp]:
            n += 1
            x43 = 43 * hamming[n]
        if x47 == hamming[rp]:
            o += 1
            x47 = 47 * hamming[o]
        if x53 == hamming[rp]:
            p += 1
            x53 = 53 * hamming[p]
        if x59 == hamming[rp]:
            q += 1
            x59 = 59 * hamming[q]
        if x61 == hamming[rp]:
            r += 1
            x61 = 61 * hamming[r]
        if x67 == hamming[rp]:
            s += 1
            x67 = 67 * hamming[s]
        if x71 == hamming[rp]:
            t += 1
            x71 = 71 * hamming[t]
        if x73 == hamming[rp]:
            u += 1
            x73 = 73 * hamming[u]
        if x79 == hamming[rp]:
            v += 1
            x79 = 79 * hamming[v]
        if x83 == hamming[rp]:
            w += 1
            x83 = 83 * hamming[w]
        if x89 == hamming[rp]:
            x += 1
            x89 = 89 * hamming[x]
        if x97 == hamming[rp]:
            y += 1
            x97 = 97 * hamming[y]
    print(hamming.index(10**9))
    return hamming[hamming.index(10**9):hamming.index(10**9)+30]

#it actually worked
