import sys


input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    m = int(input())
    data.append(m)

cnt = 0
for i in range(n - 2, -1, -1):
    if data[i] >= data[i + 1]:
        cnt += data[i] - data[i + 1] + 1
        data[i] = data[i + 1] - 1

print(cnt)
# print(data)
