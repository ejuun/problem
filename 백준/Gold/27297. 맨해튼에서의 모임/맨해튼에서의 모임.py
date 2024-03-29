import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
for i in range(M):
    dot = list(map(int, input().split()))
    for j in range(N):
        arr[j][i] = dot[j]

for i in range(N):
    arr[i].sort()

if M % 2:
    middle = (M - 1) // 2
else:
    middle = M // 2

total = 0
ans = []
for i in range(N):
    spot = arr[i][middle]
    ans.append(spot)
    for j in range(M):
        total += abs(spot - arr[i][j])

print(total)
print(*ans)