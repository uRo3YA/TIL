from collections import deque

while True:
    w, h = list(map(int, input().split()))
    if (w, h) == (0, 0):
        break

    m = []
    for _ in range(h):
        m.append(list(map(int, input().split())))
    
    visited = [[False for _ in range(w)] for _ in range(h)]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1 and not visited[i][j]:
                q = deque([(i, j)])
                cnt += 1

                while q:
                    x, y = q.popleft()
                    visited[x][y] = True

                    for dx, dy in dxy:
                        if x+dx < 0 or x+dx >= h or y+dy < 0 or y+dy >= w:
                            continue
                        if m[x+dx][y+dy] == 1 and not visited[x+dx][y+dy]:
                            q.append((x+dx, y+dy))
                            visited[x+dx][y+dy] = True
    print(cnt)