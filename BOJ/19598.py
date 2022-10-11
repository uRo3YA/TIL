import sys


input=sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, 1])  # 회의가 끝날때 1
    arr.append([e, -1])  # 회의가 끝날때 -1
arr.sort()

cnt = 0
_max = 0
for x, v in arr:
    cnt += v  # 회의실 개수 +1
    if v == 1:  # 회의가 시작일때
        _max = max(_max, cnt)  # 최댓값 갱신
print(arr)
print(_max)
