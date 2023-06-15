N, M = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(M)]

ans = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            ans[i][j] += arr1[i][k] * arr2[k][j]

for line in ans:
    print(*line)