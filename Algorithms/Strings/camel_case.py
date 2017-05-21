# count number of words in camel case text
# written by Ekaterina Boosya Gasparian
#!/bin/python3

import sys

def count_words(s):
    nb_words = 1
    for letter in s:
        if letter.isupper():
            nb_words += 1
    return nb_words

print(count_words(input().strip()))
