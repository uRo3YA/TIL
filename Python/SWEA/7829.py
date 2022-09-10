t=int(input())
for i in range(t):
    x=int(input())
    n=list(map(int,input().split()))
    print(f'#{i+1}',max(n)*min(n))