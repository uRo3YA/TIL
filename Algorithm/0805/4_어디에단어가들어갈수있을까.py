import sys

sys.stdin=open("_어디에단어가들어갈수있을까.txt")
t = int(input())

for tc in range(1,t+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]  # 검정색=0, 흰색=1
    answer = 0

    # 가로부터 탐색
    for i in range(n):
        cnt = 0
        for j in range(n):
            if board[i][j] == 0:
            	# 11101인 경우 예외처리
                if cnt == k:
                    answer += 1
                cnt = 0
                continue
            cnt += 1

        if cnt == k:
            answer += 1

    # 세로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if board[j][i] == 0:
                if cnt == k:
                    answer += 1
                cnt = 0
                continue
            cnt += 1

        if cnt == k:
            answer += 1

    print(f"#{tc}", answer)