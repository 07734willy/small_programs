import math
def distance(p1, p2):
	R = 6371 # mean radius of Earth in km
	
	cphi_1 = math.cos(math.radians(p1[0]))
	cphi_2 = math.cos(math.radians(p2[0]))

	d_phi = math.radians(p2[0] - p1[0])
	d_lam = math.radians(p2[1] - p1[1])

	a =  math.sin(d_phi / 2) ** 2
	a += math.sin(d_lam / 2) ** 2 * cphi_1 * cphi_2
	return 2 * R * math.atan2(abs(a) ** 0.5, abs(1 - a) ** 0.5)


if __name__ == "__main__":
	print(distance((40.2342, -17.9834),(13.3298, -53.1698)))
