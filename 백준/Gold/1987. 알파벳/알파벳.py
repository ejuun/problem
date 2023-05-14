def dfs(x, y):
    global ans

    if ans == 26:
        return

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and arr[nx][ny] not in sets:
                visited[nx][ny] = 1
                sets.add(arr[nx][ny])
                if ans < len(sets):
                    ans = len(sets)
                dfs(nx, ny)
                sets.remove(arr[nx][ny])
                visited[nx][ny] = 0

R, C = map(int, input().split())
arr = [list(map(str, input())) for _ in range(R)]

visited = [[0 for _ in range(C)] for _ in range(R)]
visited[0][0] = 1

sets = set()
sets.add(arr[0][0])
ans = 1

dfs(0, 0)
print(ans)