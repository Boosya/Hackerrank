# Function flip bits of 32-bit int
# Written by Ekaterina Boosya Gasparrian

def flip_bits(n):
    ones = 0xFFFFFFFF # get a 32 bits of 1111...111
    return ones - n

nb_lines = int(input())
for _ in range(nb_lines):
    n = int(input())
    print(flip_bits(n))
