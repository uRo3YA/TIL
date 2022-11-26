for tc in range(1, 11):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    cnt = 0
    for x in range(n):
        flag = 0
        for y in range(n):
            if matrix[y][x] == 1:
                flag = 1
            elif matrix[y][x] == 2:
                if flag:
                    cnt += 1
                    flag = 0
    print(f"#{tc}", cnt)
