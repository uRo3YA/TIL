n,a,b=map(int,input().split())
cnt=0
while(a!=b):
    a-=int(a//2)
    b-=int(b//2)
    cnt+=1
print(cnt)