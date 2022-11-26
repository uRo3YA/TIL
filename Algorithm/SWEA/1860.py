for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    # n명, m초,k개
    # M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
    # 2 2 2
    # 3 4 도착하는 시간
    arr = list(map(int, input().split()))
    arr.sort()
    result = "Possible"
    # x초까지 만들어진 붕어 개수: (x // M) * K
    for i in range(N):
        boong = (arr[i] // M) * K - (i + 1)
        if boong < 0:
            result = "Impossible"
            break

    print("#{} {}".format(tc, result))
