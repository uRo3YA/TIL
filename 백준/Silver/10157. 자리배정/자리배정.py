m,n = map(int,input().split())
k = int(input())
if k > m*n: # 배열의 범위를 벗어남
    print(0)
    exit()
    
board = [[0]*m for _ in range(n)]
board[0][0] = 1
move = [(1,0),(0,1),(-1,0),(0,-1)]
cur_dir = 0
x,y = (0,0)
for i in range(2,k+1):
    while True:
        a,b = move[cur_dir]
        dx = x+a; dy = y+b
        if n>dx>=0 and m>dy>=0 and board[dx][dy] == 0:
            board[dx][dy] = i
            x=dx
            y=dy # 현재 위치 갱신
            break
        else:
            cur_dir = (cur_dir+1)%4 # 방향전환
print(y+1,x+1)