while True:
    words = input("Enter the text: ")
    if words == 'cancel':
        break
    max = 0
    words = words.lower().split()
    unique_words = set(words)

    for item in unique_words:
        freq = words.count(item)
        if freq > max:
            max = freq

    for item in unique_words:
        if words.count(item) == max:
            print('{} - {}'.format(max, item))
print("Bye!")
