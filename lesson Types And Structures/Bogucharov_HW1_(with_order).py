"""

This program stores the order of words in the string

"""

words = input("Enter the text: ").split(' ')
unique_words = []
for item in words:
    if item not in unique_words:
        unique_words.append(item)
        print(item, end=' ')
