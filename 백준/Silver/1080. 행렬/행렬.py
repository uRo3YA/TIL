N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for j in range(N)]
B = [list(map(int, input().rstrip())) for j in range(N)]
cnt = 0


def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = 1 - A[x][y]


for i in range(N - 2):  
    for j in range(M - 2): 
        if A[i][j] != B[i][j]:
            flip(i, j)
            cnt += 1

        if A == B:
            break
    if A == B:
        break

if A != B:
    print(-1)
else:
    print(cnt)