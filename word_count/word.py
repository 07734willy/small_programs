import string

with open("test.txt") as file:
	text = file.read().lower()
	print({word:text.count(word) for word in text.split(" ")})
