
size = 16

def printMatrix(matrix):
	for row in matrix:
		print(row)
"""
matrix = []
for i in range(size):
	matrix.append([(i, x) for x in range(size)])

printMatrix(matrix)

print("========================")
"""
def shiftMatrixHoriz(matrix):
	newMatrix = []
	for i in range(len(matrix)//2):
		#newMatrix.append([val for pair in zip(matrix[i],matrix[i+1]) for val in pair])
		newMatrix.append([val for pair in zip(matrix[i],matrix[i+len(matrix)//2]) for val in pair])

	return newMatrix

def shiftMatrixVert(matrix):
	newM2 = []
	for i in range(len(matrix)):
		newM2.append(matrix[i][:len(matrix)*2])
		newM2.append(matrix[i][len(matrix)*2:])
	
	return newM2

def newShift(matrix, n):
	m = []
	for i in range(len(matrix)//n):
		#m.append([val for tup in zip(*matrix[i:i+n]) for val in tup])
		m.append([val for tup in zip(*matrix[i::len(matrix)//n]) for val in tup])
	
	matrix = m
	printMatrix(matrix)
	m2 = []
	for i in range(len(matrix)):
		for j in range(n):
			m2.append(matrix[i][len(matrix)*j*n:n*len(matrix)*(j+1)])

	return m2


#matrix = shiftMatrixHoriz(matrix)
#matrix = shiftMatrixVert(matrix)
#matrix = shiftMatrixHoriz(matrix)
#matrix = shiftMatrixVert(matrix)
#matrix = newShift(matrix, 4)
#printMatrix(matrix)

sqrt9 = 3
sz = 9
M = []
for i in range(sz):
	M.append([0]*sz)

for i in range(sz):
	for j in range(sz):
		#val = j // sqrt9 + sqrt9 * ((i + sz * j) % (sz * sqrt9))
		#val = j // sqrt9 + sqrt9 * (i % (sz * sqrt9)) + sqrt9 * sz * (j % sqrt9)
		val = j // sqrt9 + sqrt9 * (i + sz * (j % sqrt9))
		#print(i + j * sz, val)
		vi = (j // sqrt9 + sqrt9 * i) % sz
		vj = (j // sqrt9 + sqrt9 * i) // sz + sqrt9 * (j % sqrt9)
		#print((i,j), (val % sz, val // sz))
		#print((i,j), (vi, vj))
		M[i][j] = (val % sz, val // sz)

printMatrix(M)
