N = int(input())
def go(x):
    if x == 2:
        return -1
    return x
a = list(map(go, map(int, input().split())))
dp = [[0] * N for _ in range(2)] # [0]최대 [1]최소 dp   
dp[0][0] = a[0] # 최대 memo 
dp[1][0] = a[0] # 최소 memo

for i in range(1, N):
    # 최대 ~ 연속된 합의 최대값 구하는문제??
    if dp[0][i - 1] + a[i] > a[i]:
        dp[0][i] = dp[0][i - 1] + a[i]
    else: dp[0][i] = a[i]
    # 최소
    if dp[1][i - 1] + a[i] < a[i]:
        dp[1][i] = dp[1][i - 1] + a[i] 
    else: dp[1][i] = a[i]
print(max(max(dp[0]), abs(min(dp[1]))))