from itertools import permutations

a, b, c = map(int, input().split())
target = int(input())

operators = ["({}+{})","({}-{})","({}*{})","({}/{})","({}**{})","({}**(1.0/{}))"]

best = a + b + c
solution = operators[0].format(a, operators[0].format(b, c))

for n1, n2, n3 in permutations([a, b, c]):
	for op1 in operators:
		exprLeft  = op1.format(n1, n2)
		exprRight = op1.format(n2, n3)
		for op2 in operators:
			eLeft  = op2.format(exprLeft, n3)
			eRight = op2.format(n1, exprRight)
			
			for expr in eLeft,eRight:
				try:
					value = eval(expr)
					if abs(value - target) < abs(best - target):
						best = value
						solution = expr
				except:
					pass

print(solution)

