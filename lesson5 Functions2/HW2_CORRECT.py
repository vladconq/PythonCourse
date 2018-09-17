def my_sqrt(n, precision=None):
    if not precision:
        precision = n - int(n)
    lo, hi = 0.0, max(n, 1.0)
    prev, mid = 0, (lo + hi) / 2.0
    while abs(mid - prev) > precision:
        prev, mid = mid, (mid + (n / mid)) / 2.0
    return '{:.3g}'.format(mid)


print(my_sqrt(4))
print(my_sqrt(5, 0.01))
print(my_sqrt(4 / 10000))
print(my_sqrt(4 / 1000000))
print(my_sqrt(100))
print(my_sqrt(10e6))
print(my_sqrt(4e-128))
