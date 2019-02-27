M10 = {
    0 : ([], [0]),
    1 : ([], [1]),
    2 : ([], [2, 4, 8, 6]),
    3 : ([], [3, 9, 7, 1]),
    4 : ([], [4, 6]),
    5 : ([], [5]),
    6 : ([], [6]),
    7 : ([], [7, 9, 3, 1]),
    8 : ([], [8, 4, 2, 6]),
    9 : ([], [9, 1])
}

M4 = {
	0: ([], [0]),
	1: ([], [1]),
	2: ([2], [0]),
	3: ([3], [1])
}

M2 = {
	0: ([], [0]),
	1: ([], [1])
}

M1 = {
	0: ([], [0])
}

cycles = {10: M10, 4:M4, 2:M2, 1:M1}

cycles2 = {10:[4]

"""

	digits = []
	start = digit = values[0] % base
	while digit not in digits:
		digits.append(digit)
		digit = (digit * start) % base
	idx = digits.index(digit)
"""

def recur_mod(values, base, min_val=0):
	pre, cyc = cycle[base][values[0] % base]
	power, is_cyc = recur_mod(values[1:], len(cyc), len(pre))
	if power < len(digits)
		return digits[power]
	return digits[idx + (power % (len(digits) - idx))]
