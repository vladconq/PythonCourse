from time import time, sleep
import requests
from functools import wraps

cache = dict()


def make_cache(t):
    def decor(f):
        @wraps(f)
        def inner(*args, **kwargs):
            key = '_'.join(list(args) + list(kwargs.values())) + f.__name__
            data = cache.get(key, False)
            if data and data['time'] >= int(time()):
                return data['return']
            result = f(*args, **kwargs)
            d = {'return': result, 'time': int(time()) + t}
            cache[key] = d
            return result

        return inner

    return decor


sites = ['https://stackoverflow.com', 'https://www.youtube.com/', 'https://docs.python.org/', 'https://github.com/']


@make_cache(10)
def check_code(site):
    try:
        r = requests.head(site)
        return r.status_code, r.url
    except requests.ConnectionError:
        print("failed to connect")


for site in sites:
    print(check_code(site))
for site in sites:
    print(check_code(site))
sleep(10)
for site in sites:
    print(check_code(site))
print(check_code('https://stackoverflow.com'))
print(check_code('https://stackoverflow.com'))
print(check_code('https://github.com'))
