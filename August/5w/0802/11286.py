# 18
# 1
# -1
# 0
# 0
# 0
# 1
# 1
# -1
# -1
# 2
# -2
# 0
# 0
# 0
# 0
# 0
# 0
# 0
import heapq
import sys
input=sys.stdin.readline
#heappop
heap=[]
for i in range(int(input())):
    num = int(input())
    if num:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
