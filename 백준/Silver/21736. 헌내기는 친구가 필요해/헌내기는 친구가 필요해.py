from collections import deque

N, M = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            queue.append((i, j))
            break
    if queue:
        break

cnt = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
while queue:
    x, y = queue.popleft()
    visited[i][j] = 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx <N and 0 <= ny < M:
            if not visited[nx][ny]:
                if arr[nx][ny] == 'P':
                    cnt += 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif arr[nx][ny] == 'O':
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
if not cnt:
    print('TT')
else:
    print(cnt)