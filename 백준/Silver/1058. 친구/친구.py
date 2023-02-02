n=int(input())
matrix=[]
visit=[[ False for _ in range(n)] for _ in range(n)]

for _ in range(n):
	arr=list(input())
	matrix.append(arr)
# print(matrix)
# print(visit)

for i in range(n):
	for j in range(n):
		for k in range(n):
			if j==k:
				continue
			if matrix[j][k]=="Y" or (matrix[j][i]=="Y" and matrix[i][k]=="Y"):
				visit[j][k]=True
result=0
for i in visit:
	result=max(result,sum(i))
print(result)