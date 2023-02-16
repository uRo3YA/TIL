# 스타트링크
# 첫째 줄에 F, S, G, U, D가 주어진다.
from collections import deque
F,S,G,U,D=map(int, input().split())

def bfs(s):
    q=deque([])
    q.append((s,0))
    visited=[False]*(F+1)
    visited[s]=1
    while q:
        now, cnt=q.popleft()
        if now == G:
            return cnt
        for x in ('U',"D"):
            if x=="U":
                res=now+U
            else:
                res=now-D
            if 1<=res<=F and not visited[res]:
                q.append((res,cnt+1))
                visited[res]=1
    return "use the stairs"

print(bfs(S))