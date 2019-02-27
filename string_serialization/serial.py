def serialize(words):
	return "".join(chr(len(word)) + word for word in words)

def deserialize(words):
	if not words:
		return []
	idx = ord(words[0])+1
	return [words[1:idx]] + deserialize(words[idx:])

serialized = serialize(["test", "word", "three", "hello", "world"])
print(serialized)
deserialized = deserialize(serialized)
print(deserialized)
