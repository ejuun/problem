n, k = map(int, input().split())
dp = [1e9 for _ in range(k+1)]
coins = list(set([int(input()) for _ in range(n)]))
dp[0] = 0
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[-1] == 1e9:
    dp[-1] = -1
print(dp[-1])