from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
able_virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            able_virus.append((i, j))

combi = list(combinations([i for i in range(len(able_virus))], M))

ans = 2501

def bfs(i, visited):
    global ans

    queue = deque()
    for idx in combi[i]:
        queue.append(able_virus[idx])
        visited[able_virus[idx][0]][able_virus[idx][1]] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and arr[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    able_val = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 1 and visited[i][j] == 0:
                return
            if able_val < visited[i][j]:
                able_val = visited[i][j]

    if able_val < ans:
        ans = able_val

for i in range(len(combi)):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    bfs(i, visited)

if ans == 2501:
    print(-1)
else:
    print(ans-1)