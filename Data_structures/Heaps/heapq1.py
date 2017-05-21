# Basic opreations with heap (insert, delete, print min)
# written by Ekaterina Boosya Gasparian
import heapq
h = []
nb_lines = int(input())
for _ in range(nb_lines):
    task = input().split()
    if task [0] == '1':
        # insert in a heap
        heapq.heappush(h,int(task[1]))
    elif task [0] == '2':
        # remove
        if int(task[1]) == h[0]:
            # if removing smallest element, need to make heap out of what is left again
            h.remove(int(task[1]))
            heapq.heapify(h)
        else:
            # if removing not smallest element, just remove
            h.remove(int(task[1]))

    else:
        # printing smallest element
        print(h[0])
