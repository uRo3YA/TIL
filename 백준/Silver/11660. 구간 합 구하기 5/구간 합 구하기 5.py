import sys
input = sys.stdin.readline
n,m=map(int,input().split())

mat = [[0] * (n + 1)]

for _ in range(n):
    line=list(map(int,input().split()))
    nums = [0] + line
    mat.append(nums)

# prefix sum 행렬 만들기

# 1. 행 별로 더하기
for i in range(1, n + 1):
    for j in range(1, n):
        mat[i][j + 1] += mat[i][j]

# 2. 열 별로 더하기
for j in range(1, n + 1):
    for i in range(1, n):
        mat[i + 1][j] += mat[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # (x1, y1)에서 (x2, y2)까지의 합
    # p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1]
    print(mat[x2][y2] - mat[x1 - 1][y2] - mat[x2][y1 - 1] + mat[x1 - 1][y1 - 1])

    