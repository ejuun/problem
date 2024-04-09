from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visit = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((0, 0, 0))
visit[0][0][0] = 1

while queue:
    x, y, c = queue.popleft()

    if x == N-1 and y == M-1:
        break

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] and c+1 < (K+1) and not visit[nx][ny][c+1]:
                visit[nx][ny][c+1] = visit[x][y][c] + 1
                queue.append((nx, ny, c+1))
            elif not arr[nx][ny] and not visit[nx][ny][c]:
                visit[nx][ny][c] = visit[x][y][c] + 1
                queue.append((nx, ny, c))

ans = N * M +1
for i in range(K+1):
    if visit[N-1][M-1][i]:
       if ans > visit[N-1][M-1][i]:
           ans = visit[N - 1][M - 1][i]
if ans == N * M +1:
    ans = -1
print(ans)