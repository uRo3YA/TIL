# 5
# 100 99 98
# 100 97 92
# 63 89 63
# 99 99 99
# 89 97 98
n = int(input())
score = [[], [], []]
sum = []
for i in range(n):
    a, b, c = map(int, input().split())
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)
for i in range(n):
    s_score = 0
    for j in range(3):
        if score[j].count(score[j][i]) == 1:
            s_score += score[j][i]
    sum.append(s_score)
for i in sum:
    print(i)