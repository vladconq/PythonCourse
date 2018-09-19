def letters_range(start=0, stop=None, step=1):
    result_slice = []
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    if not stop:
        stop, start = start, 'a'

    for letter in ALPHABET[ALPHABET.index(start):ALPHABET.index(stop):step]:
        result_slice.append(letter)
    print(result_slice)


letters_range('a', 'p')
