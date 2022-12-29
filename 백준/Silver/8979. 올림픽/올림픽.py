N, K = map(int, input().split())

scores = {}
for i in range(N):
    a = list(map(int, input().split()))
    scores[a[0]] = a[1:]

count = 1
for i in range(1, N+1):
    if scores[K][0] < scores[i][0]:
        count += 1
    elif scores[K][0] == scores[i][0]:
        if scores[K][1] < scores[i][1]:
            count += 1
        elif scores[K][1] == scores[i][1]:
            if scores[K][2] < scores[i][2]:
                count += 1
print(count)