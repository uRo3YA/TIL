N = int(input())
work = []
for _ in range(N):
    work.append(list(map(int, input().split())))
work.sort(key=lambda x: -x[1])
print(work)
days = [0] * 1000
for i in range(N):
    for j in range(work[i][0] - 1, -1, -1):
        if days[j] == 0:
            days[j] = work[i][1]
            break
print(sum(days))
