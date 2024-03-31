from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
cnt = 1
queue =deque()

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = cnt
            cnt += 1
            queue.append((i, j))
            if arr[i][j] == '-':
                while queue:
                    x, y = queue.popleft()
                    ny = y + 1
                    if ny < M:
                        if arr[x][ny] == "-" and not visited[x][ny]:
                            queue.append((x, ny))
                            visited[x][ny] = visited[x][y]
            else:
                while queue:
                    x, y = queue.popleft()

                    nx = x + 1
                    if nx < N:
                        if arr[nx][y] == '|' and not visited[nx][y]:
                            queue.append((nx, y))
                            visited[nx][y] = visited[x][y]

print(cnt-1)