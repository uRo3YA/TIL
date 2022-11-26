for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for x in range(n - 1):
        for y in range(x, n):
            if arr[x] == k:
                cnt += 1
            if k == arr[x] + arr[y]:
                cnt += 1
    print(f"#{tc}", cnt)
