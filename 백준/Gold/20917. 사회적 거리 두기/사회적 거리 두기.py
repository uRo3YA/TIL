for t in range(int(input())):
    n, s = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    start = 1
    end = max(data)
    ans = 0
    while start <= end:
        mid = (start + end) // 2

        pre = data[0]
        cnt = 1
        for i in range(1, n):
            if data[i] - pre >= mid:
                pre = data[i]
                cnt += 1
        
        if cnt >= s:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    print(ans)