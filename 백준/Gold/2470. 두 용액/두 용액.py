n = int(input())
arr = sorted(map(int, input().split()))  # 정렬된 용액들

def binary_search(s, target):
    global arr
    res = n
    start, end = s, n - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    return res

v1, v2 = 0, 0
best_sum = 10 ** 10
for i in range(n):
    # 이분 탐색 수행: 현재 위치(i) 이후의 용액에서 탐색, 찾는 값은 (현재 용액 * -1)
    res = binary_search(i + 1, -arr[i])
    
    # 찾은 용액의 왼쪽 용액 확인
    if i + 1 <= res - 1 < n and abs(arr[i] + arr[res - 1]) < best_sum:
        best_sum = abs(arr[i] + arr[res - 1])
        v1, v2 = arr[i], arr[res - 1]

    # 찾은 용액 확인
    if i + 1 <= res < n and abs(arr[i] + arr[res]) < best_sum:
        best_sum = abs(arr[i] + arr[res])
        v1, v2 = arr[i], arr[res]

print(v1, v2)