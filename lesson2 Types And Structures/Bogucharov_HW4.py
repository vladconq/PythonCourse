while True:
    text = input("Enter non-negative integers separated by a space: ")
    if text == 'cancel':
        break
    source_numbers = [(int(i)) for i in text.split()]
    all_numbers_from_min_to_max = range(1, max(source_numbers))
    try:
        number = min(set(all_numbers_from_min_to_max) - set(source_numbers))
    except ValueError:
        print(max(source_numbers) + 1)
    else:
        print(number)
print("Bye!")
