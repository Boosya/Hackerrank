# Function reduce string by removing 2 similar consequtive letters_stack
# written by Ekaerina Boosya Gasparian
def reduce_string(string):
    letters_stack = []
    for letter in string:
        if len(letters_stack)==0 or letter != letters_stack[-1]:
            letters_stack.append(letter)
        else:
            letters_stack.pop()
    if len(letters_stack) == 0:
        return 'Empty String'
    else:
        return ''.join(letters_stack)

print(reduce_string(input()))
