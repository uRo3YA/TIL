n=int(input())
a=list(map(int,input().split()))
now=0
b=[]
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        now+=a[i+1]-a[i]
    if a[i]>=a[i+1]:
        b.append(now)
        now=0   
    b.append(now)
print(max(b))