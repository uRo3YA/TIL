import sys
import heapq
input = sys.stdin.readline

min_heap = []

for _ in range(int(input())):
    n = int(input())
    
    if n == 0:
        if len(min_heap):
            print(-1*(heapq.heappop(min_heap)))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, -1*(n))