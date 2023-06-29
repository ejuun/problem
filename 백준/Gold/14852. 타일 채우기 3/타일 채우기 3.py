N = int(input())
dp = [[0 for _ in range(2)] for _ in range(N+2)]
if N == 1:
    dp[1][0] = 2
elif N == 2:
    dp[2][0] = 7
elif N == 3:
    dp[3][0] = 22
else:
    dp[1][0] = 2
    dp[1][1] = 2
    dp[2][0] = 7
    dp[2][1] = 9
    dp[3][0] = 22
    dp[3][1] = 31

    for i in range(4, N+2):
        dp[i][0] = (2 * dp[i-1][0] + 3 * dp[i-2][0] + 2 * dp[i-3][1] + 2) % 1000000007
        dp[i][1] = (dp[i][0] + dp[i-1][1]) % 1000000007

print(dp[N][0])