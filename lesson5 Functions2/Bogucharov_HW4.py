from collections import OrderedDict


def make_cache(maxsize):
    def decorator(func):

        cache = OrderedDict()

        def decorated(*arg, **kwargs):
            key = (*arg, None, *kwargs)
            try:
                val = cache[key]
                del cache[key]
            except KeyError:
                val = func(*arg, **kwargs)

            cache[key] = val
            if maxsize and len(cache) > maxsize:
                cache.popitem(last=False)

            return val

        return decorated

    return decorator


@make_cache(2)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))
