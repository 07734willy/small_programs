from time import time

runs = 1000

start = time()
for i in range(runs):
	for j in range(runs):
		n = (i+j)**2 - 2 * j * i
end = time()
print(end-start)
start = time()
for i in range(runs):
	for j in range(runs):
		n = (i+j)*(i-j) + 2 * j * i
end = time()
print(end-start)
start = time()
for i in range(runs):
	for j in range(runs):
		n = i**2 + j**2
end = time()
print(end-start)
start = time()
for i in range(runs):
	for j in range(runs):
		n = i*i + j*j
end = time()
print(end-start)
import math
from math import sqrt
start = time()
for i in range(runs):
	for j in range(runs):
		n = (i*i + j*j)**0.5
end = time()
print(end-start)
start = time()
for i in range(runs):
	for j in range(runs):
		n = sqrt(i*i + j*j)
end = time()
print(end-start)
start = time()
for i in range(runs):
	for j in range(runs):
		n = math.sqrt(i*i + j*j)
end = time()
print(end-start)
start = time()
for i in range(runs):
	for j in range(runs):
		n = math.pow(i*i + j*j, 0.5)
end = time()
print(end-start)
