import sys

sys.stdin = open("1208.txt")

for tc in range(1, 11):
    l = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    # print(arr)
    for i in range(l):
        arr[0] += 1
        arr[-1] -= 1
        arr.sort()
    print(f"#{tc}: ", max(arr) - min(arr))
    # print(arr)
