import random
import time
import warnings
from random import randint
from fractions import gcd
from time import time

def primes(n):
	ps, sieve = [], [True] * (n+1)
	for p in range(2, n):
		if sieve[p]:
			ps.append(p)
			for i in range(p*p, n, p):
				sieve[i] = False
	return ps


def isqrt(n):
	x = n
	while 1:
		y = (n//x + x) // 2
		if x <= y: return x
		x = y

def jacobi(a, p):
	a, t = a%p, 1
	while a != 0:
		while a%2 == 0:
			a = a/2
			if p%8 in (3, 5):
				t = -t
		a, p = p, a
		if a%4 == 3 and p%4 == 3:
			t = -t
		a = a%p
	if p == 1: return t
	else: return 0
 
def isStrongPseudoprime(n, a):
	d, s = n-1, 0
	while d%2 == 0:
		d, s = d/2, s+1
	t = pow(a, d, n)
	if t == 1:
		return True
	while s > 0:
		if t == n-1:
			return True
		t, s = (t*t) % n, s-1
	return False

def isMillerRabinPrime(n, limit=10):
	for i in range(limit):
		a = randint(2, n-1)
		if not isStrongPseudoprime(n, a):
			return False
	return True
 
def chain(n, u, v, u2, v2, d, q, m):
	k = q
	while m > 0:
		u2 = (u2*v2) % n
		v2 = (v2*v2 - 2*q) % n
		q = (q*q) % n
		if m%2 == 1:
			t1, t2 = u2*v, u*v2
			t3,t4 = v2*v, u2*u*d
			u, v = t1+t2, t3+t4
			if u%2 == 1: u = u+n
			if v%2 == 1: v = v+n
			u, v = (u/2)%n, (v/2)%n
			k = (q*k) % n
		m = m // 2
	return u, v, k
 
def selfridge(n):
	d, s = 5, 1; ds = d * s
	while 1:
		if gcd(ds, n) > 1: return ds, 0, 0
		if jacobi(ds, n) == -1: return ds, 1, (1-ds) / 4
		d, s = d+2, s*-1; ds = d * s

def isStandardLucasPseudoprime(n):
	d, p, q = selfridge(n)
	if p == 0: return n == d
	u, v, k = chain(n, 0, 2, 1, p, d, q, (n+1)/2)
	return u == 0
 
def isStrongLucasPseudoprime(n):
	d, p, q = selfridge(n)
	if p == 0: return n == d
	s, t = 0, n+1
	while t%2 == 0:
		s, t = s+1, t/2
	u, v, k = chain(n, 1, p, 1, p, d, q, t//2)
	if u == 0 or v == 0: return True
	r = 1
	while r < s:
		v = (v*v - 2*k) % n
		k = (k*k) % n
		if v == 0: return True
	return False
 
def isBaillieWagstaffPrime(n, limit = 100):
	def isSquare(n):
		s = isqrt(n)
		return s*s == n
	if n<2 or isSquare(n): return False
	for p in primes(limit):
		if n % p == 0:
			return n == p
	return isStrongPseudoprime(n, 2) \
	   and isStrongPseudoprime(n, 3) \
	   and isStrongLucasPseudoprime(n) # or standard


def try_composite(a, d, n, s):
	# test the base a to see whether it is a witness for the compositeness of n
	if pow(a, d, n) == 1:
		return False
	for i in range(s):
		if pow(a, 2**i * d, n) == n-1:
			return False
	return True # n is definitely composite

	
def is_probable_prime(n, mrpt_num_trials = 5):
	"""
	Miller-Rabin primality test.
 
	A return value of False means n is certainly not prime. A return value of
	True means n is very likely a prime.

	"""
	assert n >= 2
	# special case 2
	if n == 2:
		return True
	# ensure n is odd
	if n % 2 == 0:
		return False
	
	# write n-1 as 2**s * d
	# repeatedly try to divide n-1 by 2
	s = 0
	d = n-1
	while True:
		quotient, remainder = divmod(d, 2)
		if remainder == 1:
			break
		s += 1
		d = quotient
	assert(2**s * d == n-1)
									 
	for i in range(mrpt_num_trials):
		a = random.randrange(2, n)
		if try_composite(a, d, n, s):
			return False
		
	return True # no base tested showed n as composite

start = time()

print(is_probable_prime(643808006803554439230129854961492699151386107534013432918073439524138264842370630061369715394739134090922937332590384720397133335969549256322620979036686633213903952966175107096769180017646161851573147596390153))

end = time()
print(end-start)
start = time()

print(isBaillieWagstaffPrime(643808006803554439230129854961492699151386107534013432918073439524138264842370630061369715394739134090922937332590384720397133335969549256322620979036686633213903952966175107096769180017646161851573147596390153, 100))

end = time()
print(end-start)


