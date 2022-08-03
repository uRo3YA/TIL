from pprint import pprint
# row,col=4,3
# #row= 행,가로줄
# #col= 열,세로줄
# mat=[[0]*col for _ in range(row)]

# print(mat)

# mat2=[[i]*col for i in range(row)]
# print(mat2)

#8 7
# 4 3 2 2 1 0 1
# 3 3 3 2 1 0 1
# 2 2 2 2 1 0 0
# 2 1 1 1 1 0 0
# 1 1 0 0 0 1 0
# 0 0 0 1 1 1 0
# 0 1 2 2 1 1 0
# 0 1 1 1 2 1 0

#​matrix = [list(map(int,input().split())) for _ in range(n)]
matrix=[]

a=0
for i in range(3):
    for j in range(4):
        a+=1
        matrix.append([a])
pprint(matrix)