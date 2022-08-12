import sys

sys.stdin = open("_Flatten.txt")
T = 10

for tc in range(1, T+1):
    N = int(input())  # 덤프횟수
    box_lst = list(map(int, input().split()))  
    cnt = [0] * 101
    for i in box_lst:
        cnt[i] += 1
    min = 101
    max = 0
    for box in box_lst:
        if box < min:
            min = box
        if box > max:
            max = box
    n = 0
    while n < N:
        cnt[max] -= 1
        cnt[max-1] += 1
        cnt[min] -= 1
        cnt[min+1] += 1

        while cnt[max] == 0:
            max -= 1
        while cnt[min] == 0:
            min += 1
        n += 1
    result = max - min

    print(f"#{tc} {result}")