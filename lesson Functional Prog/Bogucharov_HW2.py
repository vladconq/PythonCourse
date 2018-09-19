def is_armstrong(number):
    split_numbers = [int(d) for d in str(number)]
    squares = list(map(lambda x: x ** len(str(number)), split_numbers))
    return sum(squares) == number


print(is_armstrong(9))
print(is_armstrong(153))
print(is_armstrong(10))
