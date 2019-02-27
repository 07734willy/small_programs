from timeit import timeit


def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

#@profile
def primes2(n):
    sqrt_n = int(n ** 0.5) + 1
    sieve = [1] * (n + sqrt_n)
    rev_sieve = [1] * (n + sqrt_n)
    p = 2
    while p <= sqrt_n:
        i, t = p, p ** 2
        while t <= n:
            while t <= n:
                r, f = rev_sieve[t], sieve[t]
                rev_sieve[t + f] = sieve[t - r] = sieve[t - r] + f
                t *= p
            i += sieve[i]
            t = p * i
        p += sieve[p]

    l = []
    p = 2
    while p <= n:
        l.append(p)
        p += sieve[p]
    return l

def primes3(n):
    sieve = list(range(1, 2 * n))
    rev_sieve = list(range(-1, 2 * n))
    p = 2
    while p ** 2 <= n:
        i, t = p, p ** 2
        while t <= n:
            while t <= n:
                rev_sieve[sieve[t]] = rev_sieve[t]
                sieve[rev_sieve[t]] = sieve[t]
                t *= p
            i = sieve[i]
            t = p * i
        p = sieve[p]

    l = []
    p = 2
    while p <= n:
        l.append(p)
        p = sieve[p]
    return l

def primes4(n):
    sieve = [2*(x+v) for x in range(0, 2 * n) for v in (1, -1)]
    p = 2
    while p ** 2 <= n:
        i = 2 * p
        t = 2 * p * p
        while t <= 2 * n:
            while t <= 2 * n:
                r, f = sieve[t+1], sieve[t]
                sieve[f+1] = r
                sieve[r] = f
                t *= p
            i = sieve[i]
            t = p * i
        p = sieve[2 * p] >> 1

    l = []
    p = 2
    while p <= n:
        l.append(p)
        p = sieve[2 * p] >> 1
    return l

def primes5(n):
    sieve = [2] * (3 * n)
    p = 2
    while p ** 2 <= n:
        i, t = 2 * p, 2 * p ** 2
        while t <= 2 * n:
            while t <= 2 * n:
                r, f = sieve[t+1], sieve[t]
                #sieve[t + f + 1] += r
                #sieve[t - r] += f
                sieve[t - r] = sieve[t + f + 1] = sieve[t - r] + f
                t *= p
            i += sieve[i]
            t = p * i
        p += sieve[2 * p] >> 1

    l = []
    p = 2
    while p <= n:
        l.append(p)
        p += sieve[2 * p] >> 1
    return l

def primes_dumb(n):
    sieve = [0] * n
    p = 2
    for i in range(2, n):
        p = sieve[i] if sieve[i] else i
        t = i + p
        try:
            while sieve[t]: t += p
            sieve[t] = p
        except: pass

    return [i for i, x in enumerate(sieve) if not x][2:]


if __name__ == "__main__":
    n = 434300
    #n = 343
    #n = 34521000
    n = 2398321
    functions = ["primes1", "primes2", "primes3", "primes4", "primes5"]
    functions = ["primes1", "primes2", "primes5", "primes_dumb"]

    #print(primes1(343))

    setup = "from __main__ import {}; n = {}"
    for fun in functions:
        print(timeit(fun+"(n)", setup=setup.format(fun, n), number=1))
        pass
        
    for fun in functions:
        #print(eval("{}({})".format(fun, n)))
        #eval("{}({})".format(fun, n))
        pass
