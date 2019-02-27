from queue import Queue

def solve(source, target):
	queue = Queue()
	path = [source]
	queue.put(path)
	while source != target:
		queue.put(path + [source * 2])
		queue.put(path + [source + 1])
		queue.put(path + [source - 1])
		
		path = queue.get()
		source = path[-1]
	return path

if __name__ == "__main__":
	print(solve(4,79))
