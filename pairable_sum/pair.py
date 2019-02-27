def isPairable(array, k):
	#if len(array) & 1:
	#	return False

	modK = [0] * k
	for n in array:
		modK[ n % k] += 1
		modK[-n % k] -= 1

		if n % k == -n % k:
			modK[n % k] ^= 1

	return not any(modK)

print(isPairable([0, 6], 6))
print(isPairable([2], 6))
print(isPairable([3], 6))
print(isPairable([4], 6))
print(isPairable([3], 7))
print(isPairable([4], 7))
print(isPairable([2, 2], 6))
print(isPairable([3, 3], 6))
print(isPairable([4, 4], 6))
print(isPairable([3, 4], 7))
print(isPairable([4, 4], 7))
print(isPairable([1,5,6,4], 7))
print(isPairable([1,5,6,4], 7))
print(isPairable([1,9,6,5], 7))
print(isPairable([8, 12], 8))
