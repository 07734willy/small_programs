from itertools import combinations
words = []
with open("./words.txt") as file:
	words = file.read().split()

anagrams = set()
for word in words:
	anagrams.add("".join(sorted(map(str,word.lower()))))

"""
lookup = dict()

for anagram in anagrams:
	letters = dict()
	for letter in anagram:
		if not letter in letters.keys():
			letters[letter] = 0
		
		key = letter + str(letters[letter])
		if not key in lookup.keys():
			lookup[key] = set()
		lookup[key].add(anagram)

		letters[letter] += 1
"""

lookup = dict()

for anagram in anagrams:
	combination = list(combinations(anagram, 3))
	combination += list(combinations(anagram, 2))
	combination += list(combinations(anagram, 1))


	for comb in combination:
		comb = "".join(comb)
		if not comb in lookup.keys():
			lookup[comb] = set()
		lookup[comb].add(anagram)

words_3L = dict()
words_2L = dict()
words_1L = dict()

for ana in anagrams:
	words_3L[ana] = set()
	words_2L[ana] = set()
	words_1L[ana] = set()

for comb in lookup.keys():
	for ana in lookup[comb]:
		if len(comb) == 3:
			words_3L[ana].update(lookup[comb] - set(ana))
		if len(comb) == 2:
			words_2L[ana].update(lookup[comb] - set(ana))
		if len(comb) == 1:
			words_1L[ana].update(lookup[comb] - set(ana))

print(list(anagrams)[422])
print(words_2L[list(anagrams)[422]])

curr_word = anagrams[422]

