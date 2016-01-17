def ackermann(m,n):
    if m == 0:
        print(m,n)
        return n+1
    elif m > 0 and n == 0:
        print(m,n)
        return ackermann(m-1,1)
    elif m > 0 and n > 0:
        print(m,n)
        p = ackermann2(m,n-1)
        return ackermann(m-1,p)

def ackermann2(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann2(m-1,1)
    elif m > 0 and n > 0:
        p = ackermann2(m,n-1)
        return ackermann2(m-1,p)

#alright this is blowing my mind, I'll come back
