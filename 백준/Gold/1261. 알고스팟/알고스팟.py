from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(M)]
crash = [[10000 for _ in range(N)] for _ in range(M)]
queue = deque()
queue.append((0, 0))

crash[0][0] = 0

while queue:
    x, y = queue.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if maze[nx][ny]:
                if crash[nx][ny] > crash[x][y] + 1:
                    crash[nx][ny] = crash[x][y] + 1
                    queue.append((nx, ny))
            else:
                if crash[nx][ny] > crash[x][y]:
                    crash[nx][ny] = crash[x][y]
                    queue.append((nx, ny))

print(crash[M-1][N-1])