import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

length = max(dp)
val = 0
for i in range(N):
    if dp[i] == length:
       val = arr[i]

ans_arr = []
for i in range(N-1, -1, -1):
    if dp[i] == length and arr[i] <= val:
        ans_arr.append(arr[i])
        length -= 1
        val = arr[i]


print(max(dp))
print(*ans_arr[::-1])