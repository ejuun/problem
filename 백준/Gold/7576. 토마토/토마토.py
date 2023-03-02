from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == -1:
            visited[i][j] = -1

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1] #상하좌우

queue = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1

while queue:
    x, y = queue.popleft()

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and not tomato[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

result = -1
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            result = 0
            break
        else:
            if result < visited[i][j]:
                result = visited[i][j]
    if not result:
        break

result -= 1

print(result)