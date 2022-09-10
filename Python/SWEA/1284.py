
t=int(input())
for i in range(t):
    p,q,r,s,w=map(int,input().split())
    a=p*w
    if w<=r:
        b=q
    else:
        #초과사용량 c
        c=(w-r)
        b=q+(c*s) 
    
    print(f'#{i+1}',min(a,b))