from collections import defaultdict

string = "steststringstestfour"
string = "abcdthisisatextwithsampletextforasampleabcd"

def find(string, indices, depth=0):
	letters = defaultdict(list)
	for i in indices:
		if i != len(string):
			letters[string[i]].append(i+1)
	
	solutions = []
	for l in letters:
		if len(letters[l]) == 1:
			continue
		soln = find(string, letters[l], depth+1)
		if depth > 2:
			soln += [("", len(letters[l]))]
		solutions += [(l+w, c) for w,c in soln]

	return solutions

def search(string):
	solutions = find(string, range(len(string)))
	words, counts = zip(*solutions)
	for word, count in solutions:
		if count - sum([c for w,c in solutions if word in w and w is not word]) > 1:
			print("'{0}' {1} times".format(word, count))
			
print(string)
search(string)
