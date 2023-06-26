n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (k+1)

for weight, value in lst:
    for i in range(k, weight-1, -1):
        dp[i] = max(dp[i], dp[i-weight]+value)

print(dp[-1])