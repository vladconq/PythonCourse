def my_sqrt(n, precision=None):
    if not precision:
        numstr = str(n)
        if 'e' in numstr:
            index = numstr.find('e') + 2
            precision = float('0.' + int(numstr[index:]) * '0' + '1')
        else:
            precision = 0.00000001
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
print(my_sqrt(1000000))
print(my_sqrt(4e-128))
