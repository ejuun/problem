from collections import deque

M, N, H = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(N*H)]

queue = deque()

visited = t[:]

for i in range(N*H):
    for j in range(M):
        if t[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0, -N, N]
dy = [0, 0, -1, 1, 0, 0]

while queue:
    x, y = queue.popleft()

    for dir in range(6):
        rx = x + dx[dir]
        ry = y + dy[dir]
        if 0 <= rx < N*H and 0 <= ry < M:
            if not visited[rx][ry] and not t[rx][ry]:
                if dir == 0 and rx % N == N - 1:
                    continue
                elif dir == 1 and rx % N == 0:
                    continue
                else:
                    visited[rx][ry] = visited[x][y] + 1
                    queue.append((rx, ry))

ans = -1

for i in range(N*H):
    for j in range(M):
        if not visited[i][j]:
            ans = 0
            break
        else:
            if ans < visited[i][j]:
                ans = visited[i][j]
    if not ans:
        break

ans -= 1

print(ans)