R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
n0, n1, n2, n3, n4 = 0, 0, 0, 0, 0
dx=[0,1,1,0]
dy=[0,0,1,1]
for x in range(R): # 행
    for y in range(C): # 열
        # out of range 방지
        if x+1 == R or y+1 == C:
            break
        
        line=""
        for i in range(4):
            a=x+dx[i]
            b=y+dy[i]
            line+=matrix[a][b]
        # 빌딩은 부술수가 없으니까 넘기고 다시 찾기(continue)
        if '#' in line:
            continue
        else:
            n = line.count('X')
            if n == 0:
                n0 += 1
            elif n == 1:
                n1 += 1
            elif n == 2:
                n2 += 1
            elif n == 3:
                n3 += 1
            elif n == 4:
                n4 += 1
print(n0)
print(n1)
print(n2)
print(n3)
print(n4)
