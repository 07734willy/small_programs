from timeit import timeit
from random import randint

@profile
def totatives(n):
    phi = int(n > 1 and n)
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    #if n is > 1 it means it is prime
    if n > 1: phi -= phi // n 
    return phi

@profile
def totatives2(n):
    phi = n if n > 1 else 0
    
    p = 2
    while p ** 2 <= n:
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
        p += 1
    
    return phi - phi // n if n > 1 else phi

@profile
def totatives2b(n):
    phi = n if n > 1 else 0
    
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
            if p ** 2 > n:
                break
    
    return phi - phi // n if n > 1 else phi

@profile
def totatives3(n):
    phi = n if n > 1 else 0
    
    if not n & 1:
        phi = phi // 2
        while not n & 1: n >>= 1

    p = 3
    while p ** 2 <= n:
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
        p += 2
    
    return phi - phi // n if n > 1 else phi

@profile
def totatives4(n):
    phi = n if n > 1 else 0
    
    if not n & 1:
        phi = phi // 2
        while not n & 1: n >>= 1

    p = 3
    while p ** 2 <= n:
        if not n % p:
            phi -= phi // p
            d, r = divmod(n, p)
            while not r:
                n, (d, r) = d, divmod(d, p)
        p += 2
    
    return phi - phi // n if n > 1 else phi

def totatives5(n):
    phi = n if n > 1 else 0
    
    if not n & 1:
        phi = phi // 2
        while not n & 1: n >>= 1

    p = 3
    while p ** 2 <= n:
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
        p += 2
    
    return phi - phi // n if n > 1 else phi

if __name__ == "__main__":
    #n = 78495322
    #n = 239442329
    n = 64378431892

    setup = "from __main__ import {}; n = {}"
    fun1 = "totatives"
    fun2 = "totatives2"
    fun3 = "totatives3"
    fun4 = "totatives4"
    #print(timeit(fun1 + "(n)", setup=setup.format(fun1, n), number=1000))
    #print(timeit(fun2 + "(n)", setup=setup.format(fun2, n), number=1000))
    #print(timeit(fun3 + "(n)", setup=setup.format(fun3, n), number=1000))
    #print(timeit(fun4 + "(n)", setup=setup.format(fun4, n), number=1000))
    
    print(totatives(n), totatives4(n))

    for i in range(1000):
        totatives(n)
        totatives2(n)
        totatives2b(n)
        totatives3(n)
        totatives4(n)

