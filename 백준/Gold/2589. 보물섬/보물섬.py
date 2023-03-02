from collections import deque

R, C = map(int, input().split())
map = [list(map(str, input())) for _ in range(R)]

def bfs(r,c):
    queue = deque()
    queue.append((r, c))

    visited = [[0 for _ in range(C)] for _ in range(R)]
    visited[r][c] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and map[nx][ny] == 'L':
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    max_val = 0
    for i in range(R):
        for j in range(C):
            if max_val < visited[i][j]:
                max_val = visited[i][j]

    return max_val

min_distance = 0
for i in range(R):
    for j in range(C):
        if map[i][j] == 'L':
            distance = bfs(i, j)
            if min_distance < distance:
                min_distance = distance

print(min_distance - 1)
