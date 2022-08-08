board = [list(map(int, input().split(" "))) for _ in range(19)]

# 우상, 우, 우하, 하 - 3가지 방향만 고려
dx, dy = [-1, 0, 1, 1], [1, 1, 1, 0]


def is_in(x, y):
    if 0 <= x < 19 and 0 <= y < 19:
        return True
    else:
        return False


def is_omok(x, y, player):
    for k in range(len(dx)):
        # 반대방향에 나랑 같은 돌이 있는 지 확인: 없어야된다.
        bx = x - dx[k]
        by = y - dy[k]
        if not is_in(bx, by) or board[bx][by] != player:
            nx = x + dx[k]
            ny = y + dy[k]
            cnt = 1
            while True:
                if is_in(nx, ny) and board[nx][ny] == player:
                    cnt += 1
                else:
                    break
                nx += dx[k]
                ny += dy[k]
            if cnt == 5:
                return True
    else:
        return False


def main():
    for i in range(19):
        for j in range(19):
            if board[i][j] != 0:
                # 오목인지 점검하기
                if is_omok(i, j, board[i][j]):
                    return board[i][j], f'{i + 1} {j + 1}'
    else:
        return 0, 0


winner, pos = main()
if winner != 0:
    print(winner)
    print(pos)
else:
    print(winner)