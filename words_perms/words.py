from itertools import combinations

word_list = ["hello", "hey", "say", "sup", "world"]
target = "helyloasyuz"

symbols = sorted([c + str(target[i+1:].count(c)) for i, c in enumerate(target)])


class Trie:
	def __init__(self, symbol):
		self.symbol = symbol
		self.words = []
		self.children = dict()
	
	def add_word(self, word):
		self.words.append(word)

	def add_child(self, symbol, trie):
		self.children[symbol] = trie

		
print(symbols)

root = Trie(None)


def print_words(symbols, node):
	for word in node.words:
		print(word)
	for sym in node.children:
		if sym in symbols:
			print_words(symbols, node.children[sym])
		
