N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
ans = arr[N-1]
for i in range(N-1, -1, -1):
    ans = max(ans, arr[i] * (N-i))
print(ans)