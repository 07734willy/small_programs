from collections import defaultdict

def standardize(string):
	exclude = set(".!?:[](){}@#$%^&*~\"'/\\")
	return "".join(c for c in string if c not in exclude).lower()

def make_table(filename):
	text = ""
	with open(filename) as f:
		text = f.read()

	logs = [log.split("] ", 1)[1] for log in text.split("\n")[:-1]]
	messages = [log.split(": ", 1) for log in logs]

	table = defaultdict(lambda: defaultdict(int))
	for name, message in messages:
		words = standardize(message).split(" ")
		for word in words:
			table[name.lower()][word] += 1
	return table

def lookup(table, name, word):
	return table[name.lower()][standardize(word)]

if __name__ == "__main__":
	table = make_table("file.txt")
	print(lookup(table, "John Doe", "You"))
