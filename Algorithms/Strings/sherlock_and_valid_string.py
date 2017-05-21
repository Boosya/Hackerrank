# checks for validity the string. A "valid" string is a string S such that for all distinct characters in S each such character occurs the same number of times in S.
# written by Ekaterina Boosya Gasparian

from collections import defaultdict

def check_for_validity(string):
    # dict will store all letters we see and how many times we saw them
    letters = defaultdict(int)
    for letter in string:
        letters[letter] += 1
    # nb_letters is a dic with key = nb of times we saw a letter and value the amount of such letters
    nb_letters = defaultdict(int)
    for nb_letter in letters.values():
        nb_letters[nb_letter] += 1
    # if more than 2 distinct occurences of letters, not valid string
    if len(nb_letters) > 2:
        return 'NO'
    # if 1 distunct occurence or empty string, return YES
    if len(nb_letters) < 2:
        return 'YES'
    # if 2 distunct occurences and the smallest occurence is just 1, return YES
    if len(nb_letters) == 2 and min(nb_letters.values()) == 1:
        return 'YES'
    return 'NO'

print(check_for_validity(input()))
