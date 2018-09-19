from copy import deepcopy


def atom(value):
    # copy the value
    hidden_var = deepcopy(value)

    def get_value():
        return hidden_var

    def set_value(new_var):
        nonlocal hidden_var
        hidden_var = deepcopy(new_var)
        return hidden_var

    def process_value(*funcs):
        nonlocal hidden_var
        for func in funcs:
            hidden_var = func(hidden_var)
        return hidden_var

    return get_value, set_value, process_value


# Tests
my_get, my_set, my_process = atom(list(range(7)))
print(my_get())
print(my_set(list(range(9))))
print(my_process(
    lambda x: filter(lambda a: a % 2 - 1, x),
    lambda x: map(lambda a: a * a, x),
    lambda x: sum(x)
))
