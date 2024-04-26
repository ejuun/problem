from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visit = [[[0, 0] for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((Hx - 1, Hy - 1, 0))
visit[Hx - 1][Hy - 1][0] = 1
D = -1

while queue:
    x, y, c = queue.popleft()

    if x == (Ex-1) and y == (Ey-1):
        D = visit[x][y][c] - 1
        break

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] and not c:
                visit[nx][ny][c+1] = visit[x][y][c] + 1
                queue.append((nx, ny, c+1))
            elif not maze[nx][ny] and not visit[nx][ny][c]:
                visit[nx][ny][c] = visit[x][y][c] + 1
                queue.append((nx, ny, c))

print(D)