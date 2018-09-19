counter = 0


def make_it_count(func, counter_name):
    def wrapper():
        globals()[counter_name] += 1
        some_func()

    return wrapper


def some_func():
    print("I am some function")


tester = make_it_count(some_func, 'counter')
tester()
print(counter)
tester()
print(counter)
tester()
print(counter)
