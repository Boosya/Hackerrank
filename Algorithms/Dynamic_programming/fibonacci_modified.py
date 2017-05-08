# returns n-th element in modified fibonacci sequence
# f[i] = f[i-2]+f[i-1]ˆ2
# written by Ekaterina Boosya Gasparian

# reading input
t0 = int(t0)
t1 = int(t1)
n = int(n)

elements = [None]*n # will store f[i]
squares = [None]*n # will store f[i]ˆ2

# initializing fisrt 2 items in fibonacci sequence
t0, t1, n = input().split()
elements[0] = t0
elements[1] = t1
squares[0] = t0**2
squares[1] = t1**2

# for each step, calculate current fiboacci item and its square
for i in range(2,n):
    elements[i] = elements[i-2] + squares[i-1]
    squares[i] = elements[i]*elements[i]
print(elements[n-1])
