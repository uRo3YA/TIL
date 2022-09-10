data=[]
n,k=map(int,input().split())
for i in range(n):
    w,v=map(int,input().split())
    data.append((w,v))
dp = [0 for _ in range(k+1)]
for item in data:
    w,v = item
    for i in range(k,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
print(dp[-1])