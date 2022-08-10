from collections import deque

def dfs(n):
    dfs_visited[n]=True
    print(n, end=" ")
    for i in graph[n]:
        if not dfs_visited[i]:
            dfs(i)

def bfs(n):
    bfs_visited[n]=True
    q=deque([n])
    while q:
        v=q.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not bfs_visited[i]:
                q.append(i)
                bfs_visited[i]=True

n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range (1,n+1):
    graph[i].sort()
#정렬 안함
# 3 4 5 2 1 
# 3 4 1 5 2
#정렬 함
# 3 1 2 5 4 
# 3 1 4 2 5
dfs_visited=[False]*(n+1)
dfs(v)
print()
bfs_visited=[False]*(n+1)
bfs(v)
