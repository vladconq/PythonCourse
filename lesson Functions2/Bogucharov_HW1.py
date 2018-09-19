def text_to_number(text, acc=0):
    if not text:
        if acc % 2 == 0:
            acc = acc // 2
            print(acc)
            return
        else:
            acc = acc * 3 + 1
            print(acc)
            return
    elif not text[0].isdigit():
        print("Не удалось преобразовать введенный текст в число.")
        return
    return text_to_number(text[1:], 10 * acc + ord(text[0]) - 48)


while True:
    some_word = input("Enter the text: ")
    if some_word == 'cancel':
        print("Bye!")
        break
    text_to_number(some_word)
