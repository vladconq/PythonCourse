ONE_MILLION_NUMBERS = 1_000_000
sum_of_palindromes = 0
for item in range(1, ONE_MILLION_NUMBERS, 2):
    str_number = str(item)
    if str_number == str_number[::-1]:
        if format(item, 'b') == format(item, 'b')[::-1]:
            sum_of_palindromes += item

print(sum_of_palindromes)

