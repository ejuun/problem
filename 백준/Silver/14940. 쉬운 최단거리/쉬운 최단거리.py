from collections import deque
n, m = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if land[i][j] == 2:
            # visited[i][j] = 1
            queue.append((i, j))
            break
    if queue:
        break

dx = [-1, 1, 0, 0] #상 하 좌 우
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m:
            if land[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if land[i][j] == 2:
            visited[i][j] = 0
        elif land[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

for line in visited:
    print(*line)