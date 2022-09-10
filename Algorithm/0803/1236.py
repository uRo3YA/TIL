n, m = map(int,input().split())
catlse = []

for _ in range(n):
    catlse.append(input())

a, b = 0, 0
#print("catlse[1][4]:",catlse[1][4])

for i in range(n):
    if "X" not in catlse[i]:
        a += 1

for j in range(m):
    if "X" not in [catlse[i][j] for i in range(n)]:
        b += 1

print(max(a ,b))