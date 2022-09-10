for _ in range(int(input())):
    N = int(input())
    list1 = set(map(int, input().split()))
    M = int(input())
    list2 = list(map(int, input().split()))
    for n in list2:
        print(1 if n in list1 else 0)