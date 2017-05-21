import heapq

n, k = [int(_) for _ in input().split()]
cookies = [int(_) for _ in input().split()]
c_heap = []
for cookie in cookies:
    heapq.heappush(c_heap,cookie)
min_el = heapq.heappop(c_heap)
second_min_el = heapq.heappop(c_heap)
if second_min_el == 0:
    print(-1)
heapq.heappush(c_heap,min_el)
heapq.heappush(c_heap,second_min_el)
nb_operations = 0
while c_heap[0] < k:
    new_cookie = 1*heapq.heappop(c_heap) + 2*heapq.heappop(c_heap)
    heapq.heappush(c_heap,new_cookie)
    nb_operations += 1
print(nb_operations)
