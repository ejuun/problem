N = int(input())
votes = list(map(int, input().split()))
votes.sort()

ans = 0
for i in range(N):
    if i <= N // 2:
        ans += votes[i] // 2
    else:
        ans += votes[i]
print(ans)