from Functions import sieve, factors
from math import factorial


def prime_factors(n):
    L1 = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            L1.append(d)
            n = n/d
        d = d + 1
    if n > 1:
        L1.append(int(n))
    return L1

def factor_count(prime_dict):
    n = 1
    for x in prime_dict:
        n *= prime_dict[x]+1
    return n

def prime_dict_to_num(prime_dict):
    p = 1
    for x in prime_dict:
        p *= x**prime_dict[x]
    return p


def get_fact_prime_dict(n):
    L1 = []
    for x in range(1, n+1):
        L1.append(prime_factors(x))

    L2 = []
    for x in L1:
        for y in x:
            L2.append(y)

    prime_dict = {}

    for x in L2:
        if x not in prime_dict:
            prime_dict[x] = 0
        prime_dict[x] += 1

    return prime_dict


def get_prime_dict(n):
    L1 = prime_factors(n)
    prime_dict = {}

    for x in L1:
        if x not in prime_dict:
            prime_dict[x] = 0
        prime_dict[x] += 1

    return prime_dict

def prime_factor_sum(prime_dict):
    return sum([prime_dict[x] for x in prime_dict])

a = get_fact_prime_dict(10)
b = get_fact_prime_dict(100)


"""
Let P be the set of all prime factors of 100!
and let A and B sets
such that
1. A union B == P (i.e. prime_dict_to_num(A) * prime_dict_to_num(B) = 100!) and 
2. prime_factor_sum(A) + prime_factor_sum(B) = prime_factor_sum(P) and
3. factor_count(A) = factor_count(B) and
4. prime_factors_to_num(A) <= prime_factors_to_num(B)

39001250856960000 ways of splitting the prime factors of 100! into 2 sets
such that 1. and 2. are true
"""

t1 = {97: 1, 2: 49, 3: 24, 5: 12, 7: 8, 17: 3, 41: 1, 11: 5, 13: 3, 79: 1, 43: 1, 37: 1, 19: 2, 59: 1, 23: 2, 83: 1, 89: 1, 47: 1, 29: 2, 31: 1}
t2 = {2: 48, 3: 24, 5: 12, 7: 8, 73: 1, 17: 2, 71: 1, 13: 4, 47: 1, 11: 4, 43: 1, 37: 1, 19: 3, 41: 1, 23: 2, 67: 1, 61: 1, 53: 1, 29: 1, 31: 2}
