N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

if N == 1:
    print(1)
else:
    for i in range(1, N):
        find = 0
        for j in range(i, -1, -1):
            if arr[j] < arr[i]:
                if dp[i] <= dp[j]:
                    find = 1
                    dp[i] = dp[j]
        if find:
            dp[i] += 1;
    print(max(dp))