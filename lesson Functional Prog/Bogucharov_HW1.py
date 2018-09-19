from functools import reduce
from math import ceil

# way 1
squares = list(filter(lambda x: (x ** (1 / 2)).is_integer(), range(1, 1_000_000)))
sum_of_squares = reduce((lambda x, y: x + y), squares)
print(sum_of_squares)

# way 2
squares = list(map((lambda x: x ** 2), range(1, ceil(1_000_000 ** (1 / 2)))))
sum_of_squares = reduce((lambda x, y: x + y), squares)
print(sum_of_squares)

# way 3
odd_numb = list(filter(lambda x: x % 2 == 1, range(1, ceil(1_000_000 ** (1 / 2)) * 2)))
squares = list(map(lambda x: (1 + x) * (odd_numb.index(x) + 1) / 2, odd_numb))
sum_of_squares = int(reduce((lambda x, y: x + y), squares))
print(sum_of_squares)
