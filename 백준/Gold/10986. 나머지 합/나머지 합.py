import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

cumul = [0 for _ in range(N)]
cumul[0] = arr[0] % M
for i in range(1, N):
    cumul[i] = (cumul[i-1] + arr[i]) % M

cnt = [0 for i in range(M)]
for i in range(N):
    cnt[cumul[i]] += 1

ans = 0
for i in range(M):
    if i == 0:
        ans += (cnt[i] * (cnt[i]+1)) // 2
    else:
        ans += ((cnt[i]-1) * cnt[i]) // 2
print(ans)