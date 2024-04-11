for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1

    for i in range(len(coins)):
        for j in range(coins[i], len(dp)):
            dp[j] += dp[j-coins[i]]
    
    print(dp[-1])