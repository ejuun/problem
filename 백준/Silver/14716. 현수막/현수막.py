from collections import deque

def bfs(i, j):
    cnt = 1
    queue = deque()
    queue.append((i, j))

    m[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if m[nx][ny]:
                    queue.append((nx, ny))
                    m[nx][ny] = 0
    return cnt

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if m[i][j]:
            ans += bfs(i, j)
print(ans)