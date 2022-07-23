n=int(input())
k=list(map(int,input().split()))
dp=[0]*n

dp[0]=k[0]
for i in range(len(k)-1):
    if dp[i]<k[i+1]:
        dp[i+1]=k[i]+k[i+1]
print(max(dp))