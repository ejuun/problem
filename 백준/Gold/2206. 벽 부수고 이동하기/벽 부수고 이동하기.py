from collections import deque

N, M = map(int, input().split())

wall = [list(map(int, input())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y, crash = q.popleft()

    if x == N-1 and y == M-1:
        break

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < N and 0 <= ny < M:
            if not wall[nx][ny] and not visited[nx][ny][crash]:
                visited[nx][ny][crash] = visited[x][y][crash] + 1
                q.append((nx, ny, crash))
                
            elif wall[nx][ny] == 1 and not crash:
                visited[nx][ny][crash+1] = visited[x][y][crash] + 1
                q.append((nx, ny, crash+1))

ans = visited[N-1][M-1][crash]
if not ans:
    ans = -1
print(ans)