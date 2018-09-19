def partial(func, *fixated_args, **fixated_kwargs):
    def wrapper(*extra_args, **extra_kwargs):
        total_args = fixated_args + extra_args
        total_kwargs = dict(fixated_kwargs)
        total_kwargs.update(extra_kwargs)
        args = str([i for i in total_args])
        kwargs = str({key: value for (key, value) in total_kwargs.items()})

        wrapper.__doc__ = "A partial implementation of " + func.__name__ + "\n" + \
                          "with pre-applied arguments being:" + "\n" + \
                          ("args: " + args if not args == '[]' else "") + \
                          (" " if not args == '[]' else "") + \
                          ("kwargs: " + kwargs if not kwargs == '{}' else "")
        return func(*total_args, **total_kwargs)

    wrapper.__name__ = "partial_" + func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


def some_function(*args, **kwargs):
    pass


print(round(3, 123123))  # 3
round_test = partial(round)
print(round_test(3.123123))  # repeats the behavior, also 3
print(round_test.__doc__)
print(round_test.__name__)
round_test2 = partial(round, ndigits=2)
print(round_test2(3.123123))  # 3.12
print(round_test2.__doc__)
print(round_test2.__name__)

print()

tester = partial(some_function, Sky='Blue')
tester()
print(tester.__doc__)
tester(21, Sky='Black', Grass='Green')  # add arg, update kwarg, add kwarg
print(tester.__doc__)
print(tester.__name__)
