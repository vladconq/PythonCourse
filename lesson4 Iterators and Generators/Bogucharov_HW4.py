import re
import random


def make_split(exp):
    new_str = re.split("([+-/*()])", exp.replace(" ", ""))
    new_str = list(filter(None, new_str))
    return new_str


def make_number_symbols(alpha_symbols):
    for item in alpha_symbols:
        if item.isalpha():
            alpha_symbols = alpha_symbols.replace(item, str(random.randint(100, 999)))
    return alpha_symbols


def brackets_trim(input_data: str) -> str:
    list_input_data = list(input_data)
    stack_of_left_brackets = []
    number_symbols = make_number_symbols(input_data)
    total = eval(number_symbols)
    number_symbols = make_split(number_symbols)

    for index in range(len(number_symbols)):
        if number_symbols[index] == '(':
            stack_of_left_brackets.append(index)
        elif number_symbols[index] == ')':
            test_expression = number_symbols
            left_index = stack_of_left_brackets.pop()
            right_index = index
            test_expression[left_index] = ''
            test_expression[right_index] = ''
            test_string_expression = ''.join(test_expression)
            test_total = eval(test_string_expression)
            if '{0:.6f}'.format(total) == '{0:.6f}'.format(test_total):
                list_input_data[left_index] = '?'
                list_input_data[index] = '?'
            test_expression[left_index] = '('
            test_expression[right_index] = ')'
    string_input_data = ''.join(list_input_data)
    string_input_data = string_input_data.replace('?', '')

    return string_input_data


print(brackets_trim("(a*(b/c)+((d-f)/k))"))
print(brackets_trim("a"))
print(brackets_trim("a+(b+c)"))
