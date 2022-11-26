for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    a = arr[:k]
    print(a)
