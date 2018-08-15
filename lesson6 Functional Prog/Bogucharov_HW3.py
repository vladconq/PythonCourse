def collatz_steps(n, count=0):
    if n < 1:
        return 'Value must be more than one'
    if n == 1:
        return count
    return collatz_steps(n * 3 + 1 if n % 2 else n // 2, count + 1)
    
print(collatz_steps(1000000))