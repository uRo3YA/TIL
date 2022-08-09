from pprint import pprint

n,m=map(int,input().split())
matrix=[[0 for col in range(n+1)] for row in range(n+1)]
matrix_2=[ []  for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    matrix[a][b]=1
    matrix_2[a].append(b)
    
print("-------")
pprint(matrix)
pprint(matrix_2)