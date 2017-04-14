# Partitioning around first element of array
# Written by Ekaterina Boosya Gasparian

def partition(A):
    pivot = A[0]
    left = [] # will store whatever is less than pivot
    right = [] # will store whatever is greater than pivot
    equal = [] # will store equal to pivot elements
    equal.append(A[0])
    # add element on right,left or equal depending on element comparison with pivot
    for i in range(1,len(A)):
        if A[i] > pivot:
            right.append(A[i])
        elif A[i] == pivot:
            equal.append(A[i])
        else:
            left.append(A[i])
    # print left, equal and right parts
    for element in left:
        print(element,' ',end = '')
    for element in equal:
        print(element, ' ',end = '')
    for element in right:
        print(element, ' ',end = '')


if __name__ == "__main__":
    n = int(input())
    arr = input()
    arr = [int(e) for e in arr.split()]
    partition(arr)
