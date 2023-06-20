N = int(input())
stairs = [0] * (N+1)
dp = [0] * (N+1)

for i in range(1, N+1):
    score = int(input())
    stairs[i] = score

dp[1] = stairs[1]
if N < 3:
    if N == 1:
        print(dp[N])
    else:
        dp[2] = stairs[1] + stairs[2]
        print(dp[N])
else:
    dp[1]= stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for i in range(3, N+1):
        # i-2번째 계단까지 갔을때 최대 값에 현재 계단의 값을 더한 값 (i-2번째 까지 연속된 계단 + 현재 값)
        # i-3번째 계단까지 갔을때 최대 값에 i-1번째 계단의 값과 현재 계단의 값을 더한 값(i-3번째 까지 연속된 계단 + i-1번째 계단의 값 + 현재 값)
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i]+stairs[i-1])

    print(dp[N])