import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1 for _ in range(len(A))]

for i in range(len(A)):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))