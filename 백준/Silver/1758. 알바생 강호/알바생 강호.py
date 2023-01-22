n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)
total = 0

for i in range(n):
    if arr[i] - i < 0:
        continue
    total += (arr[i] - i)
print(total)