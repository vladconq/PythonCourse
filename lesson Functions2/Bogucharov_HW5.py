import time
from math import sqrt

dict_of_results = {'total calls': 0, 'total time': 0}


def profiling_decorator(global_var_of_time_and_calls):
    def decorator(func):
        dict_of_each_func = {}
        is_evaluating = False

        def wrapper(num):
            nonlocal is_evaluating
            if is_evaluating:
                return func(num)
            else:
                globals()[global_var_of_time_and_calls]['total calls'] += 1
                start = time.time()
                is_evaluating = True
                try:
                    value = func(num)
                finally:
                    is_evaluating = False
                end = time.time()
                total_time = end - start
                globals()[global_var_of_time_and_calls]['total time'] += total_time
                dict_of_each_func[func.__name__] = total_time
                print(dict_of_each_func)
                # print(value)
                if globals()[global_var_of_time_and_calls]['total time'] == 0 and \
                        globals()[global_var_of_time_and_calls][
                            'total calls'] > 1:
                    print("Both methods in this case have the same result.")
                    return
                print("Now optimal: " + str(min(dict_of_each_func.items(), key=lambda x: x[1])))
                return

        return wrapper

    return decorator


@profiling_decorator('dict_of_results')
def fib_loop(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
    return a


@profiling_decorator('dict_of_results')
def fib_list(num):
    fib = [0, 1]
    for _ in range(2, num + 1):
        fib.append(fib[-1] + fib[-2])
    return fib.pop()


@profiling_decorator('dict_of_results')
def fib_rec(num):
    if num is 0:
        return 0
    elif num is 1:
        return 1
    else:
        return fib_rec(num - 1) + fib_rec(num - 2)


def pow(x, n, I, mult):
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
             for col_b in BT]
            for row_a in A]


@profiling_decorator('dict_of_results')
def fib_matrix(num):
    try:
        F = pow([[1, 1], [1, 0]], num, identity_matrix(2), matrix_multiply)
        return F[0][1]
    except OverflowError:
        return "Result too large"


@profiling_decorator('dict_of_results')
def fib_binet(num):
    try:
        return int((((1 + sqrt(5)) ** num) - ((1 - sqrt(5)) ** num)) / ((2 ** num) * sqrt(5)))
    except OverflowError:
        return "Result too large"


# Compare fib_rec and fib_loop
fib_rec(20)
print()
fib_loop(20)
print()
print(dict_of_results)
# Ok, fib_loop is better
dict_of_results = {'total calls': 0, 'total time': 0}
print()

# Now compare fib_loop and fib_binet
fib_loop(500)
print()
fib_binet(500)
print()
print(dict_of_results)
# Ok, in this case they are the same
dict_of_results = {'total calls': 0, 'total time': 0}
print()

# Now compare fib_list and fib_loop
fib_list(1000)
print()
fib_loop(1000)
print()
print(dict_of_results)
print()
dict_of_results = {'total calls': 0, 'total time': 0}

# Now compare fib_loop and fib_matrix
fib_loop(100000)
print()
fib_matrix(100000)
print()
print(dict_of_results)
