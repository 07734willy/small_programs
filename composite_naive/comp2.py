def isComp(n):
	comp = set()
	for i in range(2, int(n**0.25)+2):
		if i in comp:
			continue
		if n % i == 0:
			return True
		val = 2 * i
		while val**2 <= n:
			comp.add(val)
			val += i
	for i in range(max(comp), int(n**0.5)+2):
		if i in comp:
			continue
		if n % i == 0:
			return True
	return False


import math

def gcd(x, y):
	while y:
		x, y = y, x % y
	return x

def isComp2(n):
	if n in [2, 3, 5]:
		return False
	prod = 30
	i = 6
	while i ** 2 < n:
		prod *= i + 1
		prod *= i + 5
		i += 6
	return gcd(prod, n) != 1


#for i in range(2, 50):
for i in [1299827]*10000:
	#print("{}: {}".format(i, isComp2(i)))
	isComp2(i)
