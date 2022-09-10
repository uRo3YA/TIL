N = int(input())
mines = [list(input().strip()) for _ in range(N)]
flag = True
move = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
for n in range(N):
    click = list(input().strip())
    for m in range(N):
        if click[m] == 'x' and mines[n][m] == '*':
            flag = False
        elif click[m] == 'x' and mines[n][m] == '.':
            count = 0
            for x,y in move:
                if -1 < n+x and n+x < N and -1 < y+m and y+m < N and mines[x+n][y+m] == '*':
                    count += 1
            mines[n][m] = str(count)

for mine_line in mines:
    for mine in mine_line:
        if mine == '*' and flag:
            print('.', end = '')
        elif mine == '*':
            print('*', end = '')
        else:
            print(mine, end = '')
    print()