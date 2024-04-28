for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    pay = int(input())
    dp = [0 for _ in range(pay+1)]
    dp[0] = 1

    for coin in coins:
        for i in range(coin, pay+1):
            dp[i] += dp[i-coin]

    print(dp[-1])