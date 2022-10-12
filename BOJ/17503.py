import heapq, sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
# 반복 횟수 n
# 선호도의 합 M
# 선호도 v
# 도수 c
# 하루에 1병, 먹었던 맥주 다시X
# 마시는 도수레벨 보다 간레벨 높아야됨
# 선호도 채우면서 N개의 맥주 모두 마실 수 있는 최소 간레벨
beer = []
for i in range(k):
    v, c = map(int, input().split())
    beer.append([v, c])
beer = sorted(beer, key=lambda x: (x[1], x[0]))
heap = []
flav_p = 0
cnt = 0
left = 0
for be in beer:
    flav_p += be[0]
    heapq.heappush(heap, be[0])
    # print(heap)
    if len(heap) == n:
        if flav_p >= m:
            answer = be[1]
            break
        else:
            flav_p -= heapq.heappop(heap)
else:
    print(-1)
    exit()
print(answer)
# print(beer)
# ----
