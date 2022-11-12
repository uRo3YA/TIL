R, C, T = map(int, input().split())
_list = [list(map(int, input().split())) for _ in range(R)]

# 청정기 위치 찾기
cleaner_loc = []
for r in range(2, R - 2):
    if _list[r][0] == -1:
        cleaner_loc.append([r, 0])
        cleaner_loc.append([r + 1, 0])
        break
# [[2, 0], [3, 0]]
# 반시계+시계방향 탐색을 위한 설정
ccw = ((0, 1), (-1, 0), (0, -1), (1, 0))
cw = ((0, 1), (1, 0), (0, -1), (-1, 0))


def spread_dust(lst):
    next_lst = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            dust = lst[r][c]
            # 먼지가 4보다 작으면 0으로 확산
            if dust <= 4:
                continue
            temp_cnt = 0
            # 소수점 버림
            sp_dust = dust // 5
            for dr, dc in cw:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and lst[nr][nc] != -1:
                    next_lst[nr][nc] += sp_dust
                    temp_cnt += 1

            lst[r][c] -= temp_cnt * sp_dust
    # 결과 쑤셔넣음
    result = [[a + b for a, b in zip(lst[i], next_lst[i])] for i in range(R)]
    return result


def run_cleaner():
    # 반시계
    y, x = cleaner_loc[0]
    now_v = 0
    temp = 0
    for dy, dx in ccw:
        while True:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < R and 0 <= nx < C:
                # 시작 지점이면 종료
                if _list[ny][nx] == -1:
                    break
                temp = _list[ny][nx]
                _list[ny][nx] = now_v
                # 바람을 밀어냄
                # 지금 좌표에 먼지값 다음 저장
                now_v = temp
                y = ny
                x = nx
            else:
                break

    # 시계
    y, x = cleaner_loc[1]
    now_v = 0
    temp = 0
    for dy, dx in cw:
        while True:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < R and 0 <= nx < C:
                if _list[ny][nx] == -1:
                    break
                temp = _list[ny][nx]
                _list[ny][nx] = now_v
                now_v = temp
                y = ny
                x = nx
            else:
                break


for t in range(T):
    _list = spread_dust(_list)
    run_cleaner()

# 전부 합산(청정기는 -1이라 +2)
print(sum(map(sum, _list)) + 2)
