import os

files = next(os.walk("."))[2]
names = [f[:f.rindex(".")] for f in files if "." in f]
names += [f for f in files if "." not in f]
for name in set(names):
	print("{}\nTotal files found: {}".format(name, names.count(name)))
