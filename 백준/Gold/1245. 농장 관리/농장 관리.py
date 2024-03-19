from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0

def bfs(i, j):

    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    able_top = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[x][y] < arr[nx][ny]:
                    able_top = False

                elif arr[x][y] == arr[nx][ny]:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))

    return able_top

for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            if bfs(i, j):
                cnt += 1

print(cnt)