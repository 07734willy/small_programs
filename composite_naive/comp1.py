import math

def isComposite(n):
    """Straight loop."""
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            return x
    return False

_PrimeList = [2]

def isCompPL(n):
    """Recursive version."""
    for x in _PrimeList:
        if n % x == 0:
            if n == x:
                return False
            return x
    for x in range(_PrimeList[-1], int(math.sqrt(n)) + 1):
        if not isCompPL(x):
            if x > _PrimeList[-1]:
                _PrimeList.append(x)
            if n % x == 0:
                return x
    return False

def isCompSR(n):
    """Serialized recursive version."""
    l = [n]
    while (math.sqrt(l[0]) > _PrimeList[-1]):
        l.insert(0, int(math.sqrt(l[0])))
    l.insert(0, _PrimeList[-1] + 1)
    while (len(l) > 2):
        q = l.pop(0)
        for x in range(q, l[0]):
            for y in _PrimeList:
                if x % y == 0:
                    break
            else:
                _PrimeList.append(x)
    return isCompPL(n)


#for i in range(20000, 50000):
for i in [1299827]*10000:
	#print("{}: {}".format(i, isComp(i)))
	#isComposite(i)
	isCompSR(i)
