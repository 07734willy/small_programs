from collections import defaultdict

#@profile
def jacobi(a, p):
    if a < 2: return a or int(n == 1)
    
    a = a % p
    t = 1
    while a:
        while not a & 1:
            a >>= 1
            if (p + 1) & 7 > 3:
                t = -t
        if a & p & 3 == 3:
            t = -t
        a, p = p % a, a
    if p == 1:
        return t
    return 0

#@profile
def nonresidue(p):
    if p & 7 == 5: return 2
    if p % 24 == 17: return 3
    
    a = 3
    while jacobi(a, p) != -1: a += 2
    return a

#@profile
def squares(p):
    if p == 2: return 1, 1
    if p & 3 == 3: return None
    x0 = pow(nonresidue(p), (p - 1) // 4, p)
    r_new, r_old = x0, p
    
    while r_old ** 2 >= p:
        r_new, r_old = r_old % r_new, r_new
    return r_old, r_new

class NoSolution(Exception): pass

#@profile
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
#@profile
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

#@profile
def factorize(n):
    const = 1
    factors = defaultdict(int)

    while not n & 1:
        factors[2] += 1
        n >>= 1
    
    if n & 3 == 3: raise NoSolution()

    p = 3
    while n > 1 and p ** 2 <= n:
        #if p ** 4 > n and (p - 1) ** 4 <= n:
        if not p & 2044:
            if is_prime(n): break
        while not n % p:
            if n % (p * p): raise NoSolution()
            n //= (p * p)
            const *= p
        p += 2
        while not n % p:
            factors[p] += 1
            n //= p
        p += 2
    
    if n != 1:
        if n & 3 == 3: raise NoSolution()
        factors[n] += 1
    return factors, const

#@profile
def pair_factors(factors, const):
    if not factors: return {(const, const)}

    factor = factors[0]
    a, b = squares(factor)
    if len(factors) == 1:
        a *= const
        b *= const
        return {(min(a, b), max(a, b))}
    
    solutions  = {tuple(sorted([a*c + b*d, abs(a*d - b*c)])) for c, d in pair_factors(factors[1:], const)}
    solutions |= {tuple(sorted([a*c + b*d, abs(a*d - b*c)])) for d, c in pair_factors(factors[1:], const)}
    return solutions

#@profile
def pair_factors2(factors, const):
    solutions = {(0, const)}
    for factor, rep in factors.items():
        a, b = squares(factor)
        for _ in range(rep):
            new_solutions = set()
            for c, d in solutions:
                t1 = a*c + b*d
                t2 = abs(a*d - b*c)
                new_solutions.add((min(t1, t2), max(t1, t2)))
                t1 = a*d + b*c
                t2 = abs(a*c - b*d)
                new_solutions.add((min(t1, t2), max(t1, t2)))
            solutions = new_solutions
    return solutions

#@profile
def make_solutions(n):
    try:
        factors, const = factorize(n)
        #factor_list = []
        #for factor, rep in factors.items():
        #    factor_list += [factor] * rep
        return pair_factors2(factors, const)
        # do stuff
    except NoSolution:
        return None

#@profile
def iterate_squares(limit):
    z = 2
    count = 0
    while z <= limit:
        res = make_solutions(z ** 2 - 1)
        if res:
            for x, y in res:
                if x + y + z <= limit: count += 1
        z += 1
    return count

print(iterate_squares(100000))
