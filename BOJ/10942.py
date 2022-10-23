# n = int(input())
# arr = list(map(int, input().split()))
# t = int(input())
# a = []
# for i in range(t):
#     x, y = map(int, input().split())
#     c = arr[x - 1 : y]
#     if c[::-1] == c:
#         a.append(1)
#     else:
#         a.append(0)
# for j in a:
#     print(j)
# 역시나 시간초과

from pprint import pprint
import sys

input = sys.stdin.readline

n = int(input())

d = [int(i) for i in input().split()]
dp = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):  # 길이가 1
    dp[i][i] = 1

for i in range(n - 1):  # 길이가 2
    if d[i] == d[i + 1]:
        dp[i][i + 1] = 1

for l in range(2, n):  # 길이가 3 이상
    for i in range(n - l):
        if d[i] == d[i + l] and dp[i + 1][i + l - 1] == 1:
            dp[i][i + l] = 1
#
# pprint(dp)
# [[1, 0, 1, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0, 1, 0],
#  [0, 0, 1, 0, 1, 0, 0],
#  [0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 1],
#  [0, 0, 0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 0, 0, 1]]
qn = int(input())

for _ in range(qn):
    i, j = [int(a) for a in input().split()]
    print(dp[i - 1][j - 1])
