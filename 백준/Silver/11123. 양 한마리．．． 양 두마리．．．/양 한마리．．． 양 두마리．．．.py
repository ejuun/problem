from collections import deque
T = int(input())

def bfs(i, j):
    global group
    group += 1
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < H and 0 <= ny < W:
                if arr[nx][ny] == '#' and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
    return visited

for _ in range(T):
    H, W = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(H)]
    visited = [[0 for _ in range(W)] for _ in range(H)]

    group = 0

    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#' and not visited[i][j]:
                bfs(i, j)

    print(group)