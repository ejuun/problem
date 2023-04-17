N = int(input())
A = list(map(int, input().split()))

dp = [0] * (N+1)
dp[0] = 1
for i in range(1, len(A)):
    if A[i-1] < A[i]:
        max_cnt = 0
        for j in range(i-1, -1, -1):
            if A[j] < A[i]:
                if max_cnt < dp[j]:
                    max_cnt = dp[j]
        dp[i] = max_cnt + 1
    else:
        for j in range(i-1, -1, -1):
            if A[j] < A[i]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        if not dp[i]:
            dp[i] = 1
print(max(dp))