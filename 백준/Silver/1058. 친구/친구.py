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
			# 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나,  A와 친구이고, B와 친구인 C가 존재해야 된다.
			if matrix[j][k]=="Y" or (matrix[j][i]=="Y" and matrix[i][k]=="Y"):
				visit[j][k]=True

#결과값
result=0
for i in visit:
	result=max(result,sum(i))
print(result)