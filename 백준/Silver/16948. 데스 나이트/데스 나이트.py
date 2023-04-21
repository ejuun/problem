from collections import deque

N = int(input())
visited = [[0 for _ in range(N)] for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())

visited[r1][c1] = 1
queue = deque()
queue.append((r1, c1))

while queue:
    x, y = queue.popleft()

    for dx, dy in [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[r2][c2] - 1)
