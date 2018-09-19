while True:
    text = input("Enter numbers separated by symbols: ")
    if text == 'cancel':
        break
    total_sum = 0
    current_number = ''

    text = text.rstrip('-')
    for index in range(len(text)):
        if text[index].isdigit():
            if not current_number and text[index - 1] == '-':
                current_number = '-'
            current_number += text[index]
        elif current_number:
            total_sum += int(current_number)
            current_number = ''
    if current_number:
        total_sum += int(current_number)
    print(total_sum)
print("Bye!")