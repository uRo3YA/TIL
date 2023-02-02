from collections import deque 
def bfs(y,x):
	q=deque()
	q.append((y,x))
	matrix[y][x]=0
	while q:
		y,x=q.popleft()
		for dx, dy in d:
			X=x+dx
			Y=y+dy
			if (0<=Y<m) and (0<=X<n)  and matrix[Y][X]==1:
				q.append((Y,X))
				matrix[Y][X]=0 



m,n=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(m)]
#8방향
d=[
(-1,-1), (0,-1), (1,-1),# 상단
(-1,0),             (1,0), # 중단
(-1,1), (0,1),    (1,1) #하단
]

cnt=0
for i in range(m):
	for j in range(n):
		if matrix[i][j]==1:
			bfs(i,j)
			cnt+=1
print(cnt)