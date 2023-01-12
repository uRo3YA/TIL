from collections import deque

N, K, S = map(int, input().split())
left, right = deque(), deque()
for _ in range(N):
    a, b = map(int, input().split())
    if a < S:
        left.append((S - a, b))
    else:
        right.append((a - S, b))

left = sorted(left, key=lambda x: x[0])
right = sorted(right, key=lambda x: x[0])

answer = 0
while left:
    remain, distance = K, 0
    while remain > 0 and left:
        a = left.pop()
        if remain >= a[1]:
            remain -= a[1]
        else:
            left.append((a[0], a[1] - remain))
            remain = 0
        distance = max(distance, a[0])
    answer += distance * 2

while right:
    remain, distance = K, 0
    while remain > 0 and right:
        a = right.pop()
        if remain >= a[1]:
            remain -= a[1]
        else:
            right.append((a[0], a[1] - remain))
            remain = 0
        distance = max(distance, a[0])
    answer += distance * 2
print(answer)