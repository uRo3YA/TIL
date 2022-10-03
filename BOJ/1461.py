import sys

input = sys.stdin.readline
# 1. 책의 개수 n, 한 번에 들 수 있는 책의 개수 M
n, m = map(int, input().split())

# 2. 책의 위치
location = list(map(int, input().split()))

# 3. 0점을 기준으로 나누기
left = []
right = []

for i in location:
    if i < 0:
        left.append(i)
    elif i > 0:
        right.append(i)

# 4. 정렬하기
left.sort()
right.sort(reverse=True)

# 5.
l_move = []
r_move = []

for i in range(0, len(left), m):
    l_move.append(abs(left[i]))

for i in range(0, len(right), m):
    r_move.append(right[i])

# 6.
result = 0
maxmove = 0  # 가장 멀리 떨어진 위치

if l_move:
    maxmove = max(l_move[0], maxmove)

if r_move:
    maxmove = max(r_move[0], maxmove)

result = (sum(l_move) + sum(r_move)) * 2 - maxmove
print(result)
