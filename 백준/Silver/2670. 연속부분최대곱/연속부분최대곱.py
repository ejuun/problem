N = int(input())
arr = [float(input()) for _ in range(N)]
dp = [0] * N
dp[0] = arr[0]
for i in range(1, N):
    dp[i] = max(arr[i], dp[i-1] * arr[i])
# print(dp)
print('%0.3f' % max(dp))