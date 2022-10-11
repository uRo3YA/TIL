import sys


input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    m = int(input())
    data.append(m)
data.sort()
abs_data = []
result = 0
for j in range(1, n + 1):
    result += abs(j - data[j - 1])
    # abs_data.append((abs(j - data[j - 1])))
# print(data)
# print(sum(abs_data))
print(result)
