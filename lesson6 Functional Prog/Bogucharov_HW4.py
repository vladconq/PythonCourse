problem6 = [abs(sum(list(map(lambda x: x ** 2, range(1, 100 + 1)))) - sum(range(1, 100 + 1)) ** 2)]
print(problem6)

problem9 = [
	(a * c * (1000 - a - c), a, c, (1000 - a - c))
	for a in range(332, 1, -1) 
	for c in range(a + 2, 1000 - a) 
	if a * a + (1000 - a - c) ** 2 ==  c * c
]
print(problem9)

problem48 = [int((str(sum(pow(n, n) for n in range(1, 1000 + 1))))[-10:])]
print(problem48)

from functools import reduce

def dec(p=6):
	yield 0
	for i in range(1, p + 1):
		yield 10 ** p - 1

frac = input().split('.')[1]
problem40 = reduce(
	lambda a, b: a * b, 
	[int(frac[i]) for i in dec(1)], 
	1
)

print(problem40)


