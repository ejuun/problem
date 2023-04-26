from collections import deque

N, M = map(int, input().split())
visited = [[0 for _ in range(N)] for _ in range(N)]
s_r, s_c = map(int, input().split())

catch = 0
INF = 1e9
check = []

for _ in range(M):
    e_r, e_c = map(int, input().split())
    visited[e_r - 1][e_c - 1] = INF
    check.append((e_r-1, e_c-1))

queue = deque()
queue.append((s_r - 1, s_c - 1))
visited[s_r - 1][s_c - 1] = 1

while queue:
    x, y = queue.popleft()

    for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] or visited[nx][ny] == INF:
                if visited[nx][ny] == INF:
                    catch += 1
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if catch == M:
                    break
    if catch == M:
        break
        
for e_r, e_c in check:
    print(visited[e_r][e_c]-1, end=' ')