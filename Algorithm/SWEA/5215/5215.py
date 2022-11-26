import sys

sys.stdin = open("sample_input.txt")


def dfs(idx, score, cal):
    global best_score
    # 정해진 칼로리를 넘어설 경우 리턴
    if cal > L:
        return
    # 최고 점수를 넘는다면 갱신해준다.
    # print(best_score, score)
    if score > best_score:
        best_score = score
    # 인덱스가 N에 도달하면 리턴
    if idx == N:
        return
    # 재료를 넣지 않는 경우
    dfs(idx + 1, score, cal)
    # 재료를 넣는 경우
    dfs(idx + 1, score + arr[idx][0], cal + arr[idx][1])


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    arr = []
    best_score = 0
    score = 0
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    dfs(0, 0, 0)
    print(f"#{tc}", best_score)
    # print(arr)
