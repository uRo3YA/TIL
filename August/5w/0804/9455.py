# for _ in range(int(input())):
#     m,n=map(int,input().split())
#     grid=[[]for _ in range(n)]
#     for i in range(m):
#         a=list(input().split())
#         for j in range(n):
#             grid[j].append(a[j])
#     movecnt=0
#     for i in range(n):
#         boxnum=grid[i].count('1')
#         floor=m-1
#         for j in range(m-1,-1,-1):
#             if grid[i][j]=="1":
#                 movecnt+=floor-j
#                 floor-=1
#     print(movecnt)

t= int(input())
for _ in range(t):
    m,n=map(int,input().split())
    box_list=[]
    for i in range(m):
        line=list(map(int,input().split()))
        box_list.append(line)
    movecnt=0    
    #열 순회
    for x in range(n):
        # 행 순회
        #  4 -> -1
        for y in range(m-1, -1, -1):
            if box_list[y][x] == 1: # 현재 탐색 좌표가 1일때
                # 조건 1) 현재 박스 아래에 박스가 없어야 한다.
                # 조건 2) 박스는 리스트의 범위를 벗어나면 안된다. 
                while y+1 != m and box_list[y+1][x] !=1:
                    # 현재 좌표는 0으로 다음 좌표는 1로 치환
                    box_list[y][x] =0
                    box_list[y+1][x] =1
                    # 
                    y+=1
                    movecnt+=1
                    
    print(movecnt)