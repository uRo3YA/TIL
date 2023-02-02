n1,n2=map(int,input().split())
l1=list(input())
l2=list(input())
# l1=l1[::-1]
l1.reverse()
t=int(input())
# print(l1+l2)
total=l1+l2

for _ in range(t):
	for i in range(len(total)-1):
		if total[i] in l1 and total[i+1] in l2:
			total[i],total[i+1]=total[i+1],total[i]
			if total[i+1]==l1[-1]:
				break

print(*total, sep="")