N = int(input())

#N 번째 자리수에서 0~9까지 경우의 수
dp = [[0 for _ in range(10)] for _ in range(N + 1)]

#1번째 자리 수에 0~9까지 가능한 계단 수
for i in range(1, 10):
    dp[1][i] = 1
    
#2번째 자리부터 0~9까지 가능한 계단 수
for i in range(2, N + 1):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1000000000)