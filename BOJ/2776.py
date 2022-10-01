for _ in range(int(input())):
    N = int(input())
    list1 = set(map(int, input().split()))
    M = int(input())
    list2 = list(map(int, input().split()))
    # 기준이 M이니 N에서 중복 다 날려버리고 하나씩 체크
    for n in list2:
        print(1 if n in list1 else 0)
