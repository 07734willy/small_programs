
def tri(num):
	return num * (num + 1) // 2

def make_list(size, depth=1):
	shape = " " * (size - depth - 1)
	shape += " ".join((str(tri(depth) - x) for x in range(depth)))
	if depth == size:
		return []
	return make_list(size, depth + 1) + [shape]

def print_dia(size):
	dia = make_list(size)
	print("\n".join(dia[::-1]))
	print("\n".join(dia))

if __name__ == "__main__":
	print_dia(5)
