from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((0, 0, 0, 0))
    visit[0][0][0] = 0

    while queue:
        x, y, c, t = queue.popleft()

        if x == N - 1 and y == M - 1:
            return t

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if t + 1 <= T:
                    if not arr[nx][ny] and visit[nx][ny][c] == -1:
                        visit[nx][ny][c] = visit[x][y][c] + 1
                        queue.append((nx, ny, c, t+1))
                    elif arr[nx][ny] == 2 and visit[nx][ny][c] == -1:
                        visit[nx][ny][c+1] = visit[x][y][c] + 1
                        visit[nx][ny][c] = visit[x][y][c] + 1
                        queue.append((nx, ny, c+1, t+1))
                    if c and arr[nx][ny] == 1 and visit[nx][ny][c] == -1:
                        visit[nx][ny][c] = visit[x][y][c] + 1
                        queue.append((nx, ny, c, t+1))
    return 'Fail'

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[[-1, -1] for _ in range(M)] for _ in range(N)]
print(bfs())