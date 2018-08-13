import time

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
                print("Now optimal: " + str(min(dict_of_each_func.items(), key=lambda x: x[1])))
                return value

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


fib_rec(20)
print()
fib_loop(20)
print()
print(dict_of_results)
print()
dict_of_results = {'total calls': 0, 'total time': 0}

fib_list(1000)
print()
fib_loop(1000)
print()
print(dict_of_results)
