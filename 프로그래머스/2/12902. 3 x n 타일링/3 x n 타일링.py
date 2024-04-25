def solution(n):
    answer = 0
    
    dp = [0] * (n+1)
    # dp[0] = 1
    dp[2] = 3
    for i in range(4, n+1, 2):
        temp = 0
        for j in range(i-4, -1, -2):
            temp += dp[j] * 2
        dp[i] = (dp[i-2] * 3 + temp + 2) % 1000000007
    
    answer = dp[n]
    return answer