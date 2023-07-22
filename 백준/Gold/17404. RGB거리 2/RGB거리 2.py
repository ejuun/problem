N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = inf = 1e9

for i in range(3):
    dp = [[inf for _ in range(3)] for _ in range(N)]
    dp[0][i] = arr[0][i]

    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + arr[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + arr[j][1]
        dp[j][2] = min(dp[j-1][1], dp[j-1][0]) + arr[j][2]

    for k in range(3):
        if i != k:
            ans = min(ans, dp[-1][k])

print(ans)