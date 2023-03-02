from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input()))for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((0, 0))

visited[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    if x == N-1 and y == M-1:
        break
        
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and maze[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[N-1][M-1])