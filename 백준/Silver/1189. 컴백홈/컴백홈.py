R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
visited[R - 1][0] = 1

ans = 0

def back(x, y, move):
    global ans, visited

    if x == 0 and y == C-1 and visited[x][y] == K-1:
        ans += 1
        return

    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and arr[nx][ny] != 'T':
                visited[nx][ny] = move + 1
                back(nx, ny, visited[nx][ny])
                visited[nx][ny] = 0

back(R-1, 0, 0)
print(ans)