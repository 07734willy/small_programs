from heapq import heappush, heappop
from itertools import chain, combinations, product
from collections import Counter
from functools import reduce
from operator import mul
import math
import time

# Requires a**3 + b**3 == c**3 + d**3
def sondat1(a, b, c, d):
    a, b = -a, -b
    p = a + b + c + d
    q = a**2 + b**2 - c**2 - d**2
    return a*p-q, b*p-q, -c*p-q, -d*p-q

# Requires a**3 + b**3 == c**3 + d**3
def sondat2(a, b, c, d):
    c, d = -c, -d
    p = a + b + c + d
    q = a**2 + b**2 - c**2 - d**2
    return a*p-q, b*p-q, -c*p-q, -d*p-q

# No requirements
def euler(a, b, c, d):
    p = 3 * (b*c - a*d) * (c**2 + 3*d**2)
    q = (a**2 + 3*b**2)**2 - (a*c + 3*b*d) * (c**2 + 3*d**2)
    r = 3 * (b*c - a*d) * (a**2 + 3*b**2)
    s = -(c**2 + 3*d**2)**2 + (a*c + 3*b*d) * (a**2 + 3*b**2)
    return p+q, p-q, r+s, r-s

# Requires a**3 + b**3 == c**3 + d**3
def piezas1(a, b, c, d, x, y):
    a, b = -a, -b
    v1 = c**2 - d**2
    v2 = a**2 - b**2
    w  = (a+b) * (c+d)
    return a*x**2-v1*x*y+b*w*y**2, b*x**2+v1*x*y+a*w*y**2, -(c*x**2+v2*x*y+d*w*y**2), -(d*x**2-v2*x*y+c*w*y**2)

# No Requirements
def piezas2(a, b, c, x, y):
    a, b = -a, -b
    d = a + b - c
    u1 = c - d
    u2 = a - b
    return a*x**2+u1*x*y+b*y**2, b*x**2-u1*x*y+a*y**2, -(c*x**2-u2*x*y+d*y**2), -(d*x**2+u2*x*y+c*y**2)

# Requires a**3 + b**3 == c**3 + d**3
def werebrusow(a, b, c, d):
    return -a**2*d+b*c**2, a*d**2-b**2*c, c*(a*b-c*d), d*(a*b-c*d)

# Validates a**3 + b**3 == c**3 + d**3
def validate_equality(a, b, c, d):
    return a**3 + b**3 == c**3 + d**3

# Validates all pairs are >= 0
def validate_sign(pairs):
    #return all(x >= 0 for x in (a, b, c, d))
    #return (a >= 0 and b >= 0) or (c >= 0 and d >= 0)
    return all(a >= 0 and b >= 0 for a, b in pairs)

# Validates a**3 + b**3 <= N
def validate_magnitude(n, a, b):
    return a**3 + b**3 <= n

def validate_nontrivial(a, b, c, d):
    return a != -b and a != c and a != d

def brute(n):
    heap = []
    heappush(heap, (0, (0, 0)))
    
    values = []
    cube_pairs = []
    while heap:
        value, (a, b) = smallest = heappop(heap)
        
        if a != b:
            heappush(heap, (a ** 3 + (b + 1) ** 3, (a, b + 1)))
        if b == 0 and a <= n:
            heappush(heap, ((a + 1) ** 3, (a + 1, 0)))

        if cube_pairs and cube_pairs[0][0] != value:
            if len(cube_pairs) > 1:
                #print(" == ".join(["{}**3 + {}**3".format(x, y) for _, (x, y) in cube_pairs]))
                values.append(code_pairs[0][0])
            cube_pairs = [smallest]
        else:
            cube_pairs.append(smallest)

    return values

#@profile
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def factors_from_decomp(prime_factors):
    n = reduce(mul, prime_factors)
    prime_factors.sort()

    size = 0
    tmp = 1
    while tmp < n:
        tmp *= prime_factors[size]
        size += 1

    factors = set([])
    for r in range(size+1):
        factors |= {reduce(mul, comb, 1) for comb in combinations(prime_factors, r)}
    
    cube_root_n = (4 * n) ** (1.0/3)
    return [f for f in factors if f <= cube_root_n]

#@profile
def factors_from_decomp2(prime_factors):
    n = reduce(mul, prime_factors)
    counter = Counter(prime_factors)
    prime_factors = sorted(list(set(prime_factors)))

    #counts = [counter[p] for p in sorted(list(set(prime_factors)))]
    #powers = product(*[range(counter[p]+1) for p in prime_factors])
    factors_list = product(*[[p ** x for x in range(counter[p]+1)] for p in prime_factors])
    #factors_list = [[pf ** pw for pf, pw in zip(prime_factors, pwr)] for pwr in powers]
    #factors_list = [[pf ** pwr[i] for i, pf in enumerate(prime_factors)] for pwr in powers]
    factors = {reduce(mul, comb, 1) for comb in factors_list}
    
    cube_root_n = (4 * n) ** (1.0/3)
    return {f for f in factors if f <= cube_root_n}

def factors_from_decomp3(prime_factors):
    n = reduce(mul, prime_factors)
    counter = Counter(prime_factors)
    prime_factors = sorted(list(set(prime_factors)))
    cube_root_n = (4 * n) ** (1.0/3)
    
    factors_list = product(*[[p ** x for x in range(counter[p]+1)] for p in prime_factors])
    
    factors = set([])
    for comb in factors_list:
        prod = 1
        for f in comb:
            prod *= f
            if prod > cube_root_n:
                continue
        factors.add(prod)
    return factors
    #factors = {reduce(mul, comb, 1) for comb in factors_list}
    
    #return [f for f in factors if f <= cube_root_n]

#@profile
def factorize(n, primes):
    idx = 0
    factors = []
    while n > 1 and primes[idx] ** 2 <= n:
        while n % primes[idx] == 0:
            factors.append(primes[idx])
            n //= primes[idx]
        idx += 1
    if n != 1:
        factors.append(n)
    return factors

#@profile
def is_square(n):
    sqrt = math.sqrt(n)
    return int(sqrt + 0.5) ** 2 == n

#@profile
def find_pairs(n, primes):
    prime_factors = factorize(n, primes)
    #print(prime_factors, n)
    #factors = {reduce(mul, pf, 1) for pf in set(powerset(sorted(prime_factors)))}
    #spf = sorted(prime_factors)
    #ps = set(powerset(spf))
    #factors = {reduce(mul, pf, 1) for pf in ps}
    factors = factors_from_decomp2(prime_factors)
    factors.remove(1)
    #factors.remove(n)
    
    #print(factors)

    pair_list = []
    for factor in factors:
        v = (4 * n / factor - factor ** 2) / 3
        if int(v) == v and v >= 0 and is_square(int(v)):
            #print(factor, v)
            v = int(v)
            sqrt = int(math.sqrt(v) + 0.5)
            a = (factor + sqrt) // 2
            b = (factor - sqrt) // 2
            pair_list.append((a, b))
    return pair_list

#@profile
def iterate_taxi(n=0):
    for x, y, z in product(range(n), range(n), range(n)):
        yield euler(x, y, z, n)
        yield euler(x, y, n, z)
        yield euler(x, n, y, z)
        yield euler(n, x, y, z)
    for pair in iterate_taxi(n + 1):
        yield pair

from random import randint
if __name__ == "__main__":
    primes = []
    with open("./prime_list.txt", "r") as f:
        primes = [int(x) for x in f.read().split(",")]
    
    
    #print(find_pairs(9**3 + 10**3, primes))


    values_list = [(9, 10, 12, 1)]


    for values in iterate_taxi():
        if validate_sign([values[:2], values[2:]]) and validate_nontrivial(*values) and validate_magnitude(int(3e23), *values[:2]):
            pairs = find_pairs(values[0] ** 3 + values[1] ** 3, primes)
            if len(pairs) > 2 and validate_sign(pairs):
                print(len(pairs), pairs)
    """
    while values_list:
        values = values_list.pop()
        print(validate_equality(*values), values)
        
        if not validate_magnitude(values[0], values[1], int(1e10)):
            continue

        values_list.append(piezas1(*values, 4, 6))
    """
    """
    for _ in range(10):
        old_values = [randint(-2, 2) for _ in range(4)]
        values = euler(*old_values)
        #values = euler(0, 1, 1, -1)
        print(validate_equality(*values), values, old_values)

    """
