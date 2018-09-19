"""

This program doesn't store the order of words in the string

"""

unique_words = set(input("Enter the text: ").split(' '))
for item in unique_words:
    print(item, end=' ')
