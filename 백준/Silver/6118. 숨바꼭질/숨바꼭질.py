# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
from collections import deque
def bfs(node):
    q=deque()
    q.append(node)
    distance[node]=1
    while q:
        node=q.popleft()
        for i in matrix[node]:
            if distance[i]==0:
                distance[i]=distance[node]+1
                q.append(i)



n,m=map(int,input().split())
matrix=[[] for _ in range(n+1) ]
for i in range(m):
    A_i,B_i=map(int,input().split())
    matrix[A_i].append(B_i)
    matrix[B_i].append(A_i)
distance=[0]*(n+1)
bfs(1)
m=max(distance)
print(distance.index(m),m-1,distance.count(m))
# print(matrix)

