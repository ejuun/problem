N = int(input())
dp = [0] * 31
dp[2] = 3
dp[4] = 11
if N % 2:
    print(0)
else:
    if N == 2 or N == 4:
        print(dp[N])
    else:
        for i in range(6, N+1, 2):
            dp[i] = 3 * dp[i-2] + 2
            for j in range(2, i-2, 2):
                dp[i] += 2 * dp[j]
        print(dp[N])