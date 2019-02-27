import os
import stat

count = 0
directory = "."
files = [os.path.join(r,fn) for r,d,f in os.walk(directory) for fn in f]
for filename in files:
	if os.path.islink(filename):
		mode = stat.S_IMODE(os.stat(filename)[stat.ST_MODE])
		path = os.path.realpath(filename)
		if os.path.isdir(filename):
			os.rmdir(filename)
		else:
			os.unlink(filename)
		with open(path) as src, open(filename, "w") as dest:
			dest.write(src.read())
		os.chmod(filename, mode)
		count += 1
		print("Replaced symlink: {}, with: {}".format(filename, path))
print("\nReplaced {} symlinks".format(count))
