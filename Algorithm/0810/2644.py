from collections import deque
import sys
sys.stdin=open("input.txt")
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for i in range(n + 1)]
result = [0 for i in range(n + 1)]

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [False for i in range(n + 1)]
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = True
                result[i] = result[v] + 1
                queue.append(i)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)
if result[b] != 0:
    print(result[b])
else:
    print(-1)