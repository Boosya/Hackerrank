# Partitioning around first element of array
# Written by Ekaterina Boosya Gasparian

def partition(A):
    if len(A) < 2:
        return A
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
    # recursive calls
    leftpartitioned = partition(left)
    rightpartitioned = partition(right)
    # creating resulting array
    result = []
    result.extend(leftpartitioned)
    result.extend(equal)
    result.extend(rightpartitioned)
    # print resulting array
    for element in result:
        print(element,end = ' ')
    print()
    return result

if __name__ == "__main__":
    n = int(input())
    arr = input()
    arr = [int(e) for e in arr.split()]
    partition(arr)
