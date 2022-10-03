import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

sum = 0
for i in range(n - 1):
    cmp1 = heapq.heappop(cards)
    cmp2 = heapq.heappop(cards)
    # print(cmp1, cmp2)
    cmp = cmp1 + cmp2
    heapq.heappush(cards, cmp)
    sum += cmp
print(sum)
