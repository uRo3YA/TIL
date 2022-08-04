xy_list = [[0 for _ in range(101)] for _ in range(101)]

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            xy_list[j][k] = 1

result = 0
for row in xy_list:
    result += sum(row)
    
print(result)