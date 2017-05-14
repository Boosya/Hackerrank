# Given longint x find the amuont of all such a:
# x^a > x and 0 < a < x
# Written by Ekaterina Boosya Gasparrian

import sys

def theGreatXor(x):
    answer = 0 # will count the number of such a's
    i = 0 # shifting
    while (x >> i)!= 0: # move number to the right
        if (x >> i)&1 == 0: # if the digit at position i from the rihgt is 0
            answer += 2**i # the positions to the right form this digit can be any - 0 or 1
        i += 1
    return answer

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = theGreatXor(x)
    print(result)
