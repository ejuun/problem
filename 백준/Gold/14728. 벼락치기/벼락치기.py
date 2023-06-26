N, T = map(int, input().split())

dp = [0] * (T+1)

arr = []

for _ in range(N):
    time, score = map(int, input().split())
    arr.append((time, score))

for time, score in arr:
    for i in range(T, time-1, -1):
        dp[i] = max(dp[i], dp[i-time]+score)

print(dp[-1])