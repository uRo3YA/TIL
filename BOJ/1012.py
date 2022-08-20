import sys

# 백준에서 RecursionError가 안나게한다.
sys.setrecursionlimit(10**6)


def dfs(x, y):

    # 범위를 벋어나면 나가도록 하자.
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 만약 배추가 있는곳이면 
    if data[x][y] == 1:
        
        # 방문했다는 의미로 0으로 돌려놓자.
        data[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        # 처음 들어온 값이므로 True로 리턴을 주자.
        return True
    
    return False

t = int(input())

for _ in range(t):

    m, n, k = map(int, input().split())

    data = [[0] * m for i in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        data[b][a] = 1
    
    result = 0
    for i in range(m):
        for j in range(n):

            # 처음 들어온 값에 대해서만 1을 더해준다.
            if data[j][i] == 1:
                dfs(j, i)
                result += 1

    print(result)