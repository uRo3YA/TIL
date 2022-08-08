d_y = [-1, -1, -1, 0, 0, 1, 1, 1]
d_x = [-1, 0, 1, -1, 1, -1, 0, 1]

mine_cnt = "*"
empty = "."

n = 8
# board = [
#     "...**..*",
#     "......*.",
#     "....*...",
#     "........",
#     "........",
#     ".....*..",
#     "...**.*.",
#     ".....*..",
# ]
# open_board = [
#     "xxxx....",
#     "xxxx....",
#     "xxxx....",
#     "xxxxx...",
#     "xxxxx...",
#     "xxxxx...",
#     "xxx.....",
#     "xxxxx...",
# ]

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))
    
open_board = []
for _ in range(n):
    open_board.append(list(input()))

# result_board 생성
result_board = []
for i in range(n):
    temp = ["."] * n
    result_board.append(temp)
# pprint(result_board)


board = list(board)
open_board = list(open_board)
mine_find = False

# 이중반복문
for y in range(n):
    for x in range(n):
        # 현재 위치가 오픈한 위치
        # open_board -> x
        if open_board[y][x] == "x":
            mine_cnt = 0
            for d in range(8):
                search_y = y + d_y[d]
                search_x = x + d_x[d]
                # search_y search_x의 범위는 리스트를 벗어나면 안된다.
                # 리스트의 범위는 0 ~ 7(리스트의 길이 8)

                if 0 <= search_y <= n-1 and 0<= search_x <= n-1:
                    if board[search_y][search_x] == mine_cnt:
                        mine_cnt += 1

            result_board[y][x] = str(mine_cnt)
            
            # 현재 오픈한 위치에 mine_cnt가 있는지 확인 
            if board[y][x] == mine_cnt:
                mine_find = True

# mine_cnt를 발견했으면 모든 mine_cnt의 위치를 result_board에 표시
if mine_find == True:
    for y in range(n):
        for x in range(n):
            if board[y][x] == mine_cnt:
                result_board[y][x] = mine_cnt

# pprint(result_board)
for row in result_board:
    print("".join(row))