x=int(input())
n=int(input())
rcp=[]
sum=0
for i in range(n):
    a,b=map(int,input().split())
    rcp.append(a*b)
for i in range(n):
    sum+=rcp[i]
if sum == x:
    print("Yes")
else:
    print("No")