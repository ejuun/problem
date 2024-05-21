import math
N = int(input())
prime = []
for i in range(1, int(math.sqrt(N))+1):
    prime.append(i**2)

dp = [100000 for _ in range(N+1)]
for i in range(1, N+1):
    if i in prime:
        dp[i] = 1
    else:
        for j in prime:
            if i > j:
                dp[i] = min(dp[i], dp[i-j]+1)
print(dp[N])