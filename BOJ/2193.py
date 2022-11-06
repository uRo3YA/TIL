n = int(input())

dp = [0] * (n + 1)
dp[1] = 1

# dp 점화식
# 경우의 수를 따져보면 피보나치 수열과 비슷한 형태를 띄고 있음
for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])