import sys

sys.stdin = open("_파리퇴치.txt")

#5 2
t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    k = m-1
    max_v = 0
    for i in range(n-k):
        for j in range(n-k):
            sum_v = 0
            for di in range(m):
                for dj in range(m):
                    sum_v += arr[i+di][j+dj]
            if sum_v > max_v:
                max_v = sum_v
    print(f'#{tc}', max_v)