from time import time
	
runs = 100000

start = time()
for _ in range(runs):
	x = 4
	100 ^ ((x ^ 100) & -(x < 100))
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	y = 4
	y & -(0 < y)
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	x = 4
	100 + ((x - 100) & ((x - 100) >> 31))
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	x = 4
	x - (x & (x >> 31))
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	min(4, 100)
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	max(4, 0)
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	x = 4
	if x > 100:
		x = 100
	elif x < 0:
		x = 0
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	x = 4
	x = 100 if x > 100 else 0 if x < 0 else x
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	x = 4
	((x,0),(100,100))[x > 100][x < 0]
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	x = 4
	x *= (x >= 0)
	if x > 100:
		x = 100
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	x = 4
	if x > 100:
		x = 100
	else:
		x &= ~(x >> 31)
end = time()
print("Time: {}".format(end-start))

start = time()
for _ in range(runs):
	x: int = 4
	if x > 100:
		x = 100
	elif x < 0:
		x = 0
end = time()
print("Time: {}".format(end-start))
