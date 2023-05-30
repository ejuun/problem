from collections import deque

def bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not arr[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not arr[i][j] and not visited[i][j]:
                cnt += 1
    return cnt

def make_wall(cnt):
    global max_area

    if cnt == 3:
        a = bfs()
        if max_area < a:
            max_area = a
            return
        return

    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                arr[i][j] = 1
                make_wall(cnt + 1)
                arr[i][j] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_area = 0

make_wall(0)
print(max_area)