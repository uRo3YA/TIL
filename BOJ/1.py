n = int(input())
m = []

for i in range(n):
    a, b = map(int, input().split())
    m.append([a, b])

m.sort(key = lambda x: x[0])
m.sort(key = lambda x: x[1])

cnt = 1
end = m[0][1]
for i in range(1, n):
    if m[i][0] >= end:
        cnt += 1
        end = m[i][1]
print(cnt)