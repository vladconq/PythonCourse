"""

A brief analysis of the complexity of the program:
1. Conditional checks are constant (i.e. O(1))
   Total: 1
2. List comprehension as for-loop is O(n)
   int() operation is constant, so O(1)
   text.split() loops through the string, so it's O(n) (not nested!)
   Total: O(n) + 1 + O(n) = 2*O(n) = O(n)
3. min and max functions are O(n) and are evaluated once in line
   range(n) - O(n)
   Total: 2*O(n) + O(n) = 3*O(n) = O(n)
4. min, set, set, difference
   Total: O(n) + O(n) + O(n) + O(n) = 4*O(n) = O(n)

1 + O(n) + O(n) + O(n) = O(n) - linear complexity

"""

while True:
    text = input("Enter non-negative integers separated by a space: ")
    if text == 'cancel':  # 1
        break
    source_numbers = [(int(i)) for i in text.split()]  # 2
    all_numbers_from_min_to_max = range(min(source_numbers), max(source_numbers))  # 3
    try:
        number = min(set(all_numbers_from_min_to_max) - set(source_numbers))  # 4
    except ValueError:
        print("This is a sequence without missing elements.")
    else:
        print(number)
print("Bye!")
