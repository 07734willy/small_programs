from itertools import combinations
from functools import reduce
from math import factorial

@profile
def ncr(n, r):
    if r > n: return 0
    r = min(r, n-r)
    result = reduce(int.__mul__, range(n, n-r, -1), 1)
    return result // factorial(r)

@profile
def encode(numbers):
    return sum(ncr(x, i) for i, x in enumerate(numbers, 1))

@profile
def decode(value, n=50, r=6, y=ncr(50,6)):
    if not n: return (0,) if r else tuple()
    if y <= value:
        return decode(value - y, n - 1, r - 1, y * r // n) + (n,)
    return decode(value, n - 1, r, y * (n - r) // n)

def test_all():
    numbers = list(range(0,49))
    for comb in combinations(numbers, 6):
        if comb != decode(encode(comb)):
            print("error", comb, encode(comb), decode(encode(comb)))

def main():
    test_all()

if __name__ == "__main__":
    print(encode([0, 1, 2]))
    print(decode(encode([0, 2, 3, 4, 5, 22])))
    main()

def decode_old(value):
    n, r = 50 - 1, 6
    result = []
    y = ncr(n, r)
    while value:
        while value < y:
            y = y * (n-r) // n
            n -= 1
        
        result.append(n)
        value -= y
        y = y * r // (n-r+1)
        r -= 1

    return tuple(result[::-1])
