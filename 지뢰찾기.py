# 입력
# 2개의 이차원 리스트
# 지뢰가 있는 리스트
# 열었던 리스트
n=8
board=[
   " ...**..*",
    "......*.",
    "....*...",
    "........",
    "........",
    ".....*..",
    "...**.*.",
    ".....*..",
]
open_board=[
    "xxx.....",
    "xxxx....",
    "xxxx....",
    "xxxxx...",
    "xxxxx...",
    "xxxxx...",
    "xxx.....",
    "xxxxx...",
]
#결과보드 생성
result=[]
for i in range(n):
    tmp=["."]*n
    result.append(tmp)


dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
#y,x=1,3
board=list(board)
open_board=list(open_board)
for y in range(n):
    for x in range(n):
        mine=0
        #현재 오픈 위치가 오픈한 위치

        for d in range(8):
            search_y=y+dy[d]
            search_x=x+dx[d]
            # 탐색_y,탐색_x는 범위를 벗어 나면 안된다.
            # 0~7
            if 0<= search_y<8 and 0<= search_x <8:
                if board[search_y][search_x] =="*":
                    mine+=1
        result[y][x]=mine
        #현재 오픈한 위치에 지뢰가 있는지 확인
        if board[y][x]=="*":
            mine_fine=True
if mine_fine==True:
    for y in range(n):
        for x in range(n):
            if board[y][x]=="*":
                result[y][x]=mine
for row in result:
    print("".join(str(row)))