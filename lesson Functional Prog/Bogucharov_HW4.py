#   PROBLEM 40
from functools import reduce

champ_str = ''.join(str(e) for e in [i for i in range(200000)])
print(reduce(lambda x, y: x * y, [int(champ_str[10 ** c]) for c in range(6)]))

#   PROBLEM 6
problem6 = [abs(sum(list(map(lambda x: x ** 2, range(1, 100 + 1)))) - sum(range(1, 100 + 1)) ** 2)]
print(problem6)

#   PROBLEM 9
problem9 = [
    (a * c * (1000 - a - c), a, c, (1000 - a - c))
    for a in range(332, 1, -1)
    for c in range(a + 2, 1000 - a)
    if a * a + (1000 - a - c) ** 2 == c * c
]
print(problem9)

#   PROBLEM 48
problem48 = [int((str(sum(pow(n, n) for n in range(1, 1000 + 1))))[-10:])]
print(problem48)
