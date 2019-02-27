from itertools import permutations

coeffs = list(map(int, input("Coefficents, separated by spaces:\n").split()))
target = int(input("Target value:\n"))

operators = ["({}+{})","({}-{})","({}*{})","({}/{})","({}**{})","({}**(1.0/{})"]

def make_expr(expr, coeffs, target, default):
	if not coeffs:
		try:
			return abs(target-eval(expr)), expr
		except Exception:
			return default, None
	
	solutions =  [make_expr(op.format(expr, coeffs[0]), coeffs[1:], target, default) for op in operators]
	solutions += [make_expr(op.format(coeffs[0], expr), coeffs[1:], target, default) for op in operators]
	val, expr = min(solutions, key=lambda x: x[0])
	return val, expr

def find_best(coeffs, target):
	assert(len(coeffs) > 1)
	solutions = [make_expr(perm[0], perm[1:], target, abs(target-sum(coeffs))+1) for perm in permutations(coeffs)]
	val, expr = min(solutions, key=lambda x: x[0])
	return "Closest value: {0}\nExpression: {1}".format(target - val, expr)
	
print(find_best(coeffs, target))
