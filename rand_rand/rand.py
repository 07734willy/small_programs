from random import random

def rand(T):
	bounds = None
	if T % 100 == 0:
		bounds = (15, 16)
	elif T % 10 == 0:
		bounds = (5, 6)
	elif T in [1, 2, 3]:
		bounds = (2, 3)
	elif T in [0.5, 1.5, 2.5]:
		bounds = (1, 2)
	
	lower, upper = bounds
	return random() * (upper - lower) + lower
