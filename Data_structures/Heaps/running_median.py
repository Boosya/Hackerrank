# Use heaps to calculate median on the go
# Written by Ekaterina Boosya Gasparian
import sys
import heapq
# Will keep the lowest half of elements in h_low with key = -value
# and highest half of elements in h_high with key = value
h_low=[]
h_high=[]
# read input
n = int(input())
numbers = [int(input()) for _ in range(n)]
# insert first 2 numbers in heaps
heapq.heappush(h_low,-min(numbers[1],numbers[0]))
print(numbers[0])
heapq.heappush(h_high,max(numbers[1],numbers[0]))
print((numbers[1]+numbers[0])/2)
# create length trackers for h_high and h_low
len_low = 1
len_high = 1
# while going through input list
for i in range(2,len(numbers)):
    # get item that needs to be injected
    nextItem = numbers[i]
    # to understand where it should belong, pushpop it
    # to both h_low and h_high
    lowmed = - heapq.heappushpop(h_low,-nextItem)
    highmed = heapq.heappushpop(h_high,lowmed)

    # if heaps low and high are the same size
    # median is the element we have
    # add the element to any heap
    if len_high == len_low:
        median = highmed
        heapq.heappush(h_high,highmed)
        len_high += 1
    else:
        #otherwise  insert element in shortest heap
        if len_high < len_low:
            heapq.heappush(h_high,highmed)
            len_high += 1
        else:
            heapq.heappush(h_low,-highmed)
            len_low += 1
        # then median is avg between max in low and min in high
        median = (-h_low[0] + h_high[0])/2
    print(median)
