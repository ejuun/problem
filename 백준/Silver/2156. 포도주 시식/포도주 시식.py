N = int(input())
arr = [0] * (N+1)
for i in range(1, N+1):
    arr[i] = int(input())

if N == 1:
    print(arr[1])
elif N == 2:
    print(arr[1] + arr[2])
elif N == 3:
    print(max(arr[1]+arr[3], arr[2]+arr[3], arr[1]+arr[2]))
else:
    dp = [0] * (N+1)
    dp[1] = arr[1]
    dp[2] = dp[1] + arr[2]
    dp[3] = max(dp[1]+arr[3], arr[2]+arr[3], dp[2])
    for i in range(4, N+1):
        dp[i] = max(dp[i-2], dp[i-3]+arr[i-1], dp[i-4]+arr[i-1]) + arr[i]
    print(max(dp))