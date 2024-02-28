N = int(input())

dp = [1] * 10
ans = 0
for _ in range(N-1):
    for i in range(10):
        dp[i] = sum(dp[i:]) % 10007

print(sum(dp) % 10007)