while True:
    text = input("Enter non-negative integers separated by a space: ")
    if text == 'cancel':
        break
    source_numbers = [(int(i)) for i in text.split()]
    all_numbers_from_min_to_max = list(range(1, max(source_numbers) + 1))
    new_set = set(all_numbers_from_min_to_max) - set(source_numbers)
    if not new_set:
        print(max(source_numbers) + 1)
    else:
        print(min(new_set))
print("Bye!")