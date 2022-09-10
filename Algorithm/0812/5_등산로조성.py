import sys
from collections import deque
sys.stdin = open("_등산로조성.txt")
def dfs(i, j, n, maps):
    queue = deque()
    visited = [[1] * (n) for _ in range(n)]
    graph = maps

    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]

    queue.append((i, j))

    while queue:
        y, x = queue.popleft()

        if visited[y][x]:
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]

                if -1 < ny < n and -1 < nx < n:
                    if graph[y][x] > graph[ny][nx]:
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny, nx))

    return max(map(max, visited))
    

t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())

    maps = []
    for _ in range(n):
        m = list(map(int, input().split()))
        maps.append(m)

    len_list = []
    max_height = max(map(max, maps))

    for a in range(n):
        for b in range(n):
            for c in range(1, k + 1):
                maps[a][b] -= c

                for d in range(n):
                    for e in range(n):
                        if maps[d][e] == max_height:
                            len_list.append(dfs(d, e, n, maps))

                maps[a][b] += c
    #print(set(len_list))
    print(f"#{tc}", max(len_list))