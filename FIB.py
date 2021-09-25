n, k = map(int, input().split())
dp = [0] * 50
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + k * dp[i - 2]

print(dp[n])
