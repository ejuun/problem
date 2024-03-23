n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[1 for _ in range(n)] for _ in range(n)]

order = []
for i in range(n):
    for j in range(n):
        order.append((arr[i][j], i, j))

order.sort(reverse=True)

ans = 0
for t in order:
    tree, x, y = t[0], t[1], t[2]

    tmp = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] > tree:
                tmp.append(dp[nx][ny])

    if len(tmp):
        dp[x][y] = max(tmp) + 1

    if ans < dp[x][y]:
        ans = dp[x][y]

print(ans)