n = int(input())
arr = list(map(int, input().split()))
arr.append(int(100001))

count = 0
count_max = 0

for i in range(n):
    if arr[i] > arr[i + 1]:
        arr[i + 1] = arr[i]
        count += 1

    else:
        count_max = max(count, count_max)
        count = 0  # count 초기화
print(count_max)
