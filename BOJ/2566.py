from pprint import pprint

max_num = -1
max_j, max_k = 0, 0
mat = []
for i in range(9):
    a = list(map(int, input().split()))
    mat.append(a)
for j in range(9):
    for k in range(9):
        if max_num <= mat[j][k]:
            max_num = mat[j][k]
            max_j = j
            max_k = k

print(max_num)
print(max_j + 1, max_k + 1)

# pprint(mat)
# print(mat[3][4])
