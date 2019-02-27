def ducci(seq, seen=[]):
	seq = [abs(a-b) for a,b in zip(seq, seq[1:]+[seq[0]])]
	if seq in seen:
		return len(seen) + 1, seen
	return ducci(seq, seen + [seq])

if __name__ == "__main__":
	size, seen = ducci([0, 653, 1854, 4063])
	for seq in seen:
		print(seq)
	print("{} steps".format(size))
