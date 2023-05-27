from collections import deque
arr = [[0 for _ in range(1002)] for _ in range(1002)]
visited = [[0 for _ in range(1002)] for _ in range(1002)]
x, y, n = map(int, input().split())
arr[x+500][y+500] = 1e9

for _ in range(n):
    a, b = map(int, input().split())
    arr[a+500][b+500] = -1

def bfs(x, y):
    queue = deque()
    queue.append((500, 500))
    arr[500][500] = 1
    visited[500][500] = 1

    while queue:
        mx, my = queue.popleft()

        for dx, dy in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            nx = mx + dx
            ny = my + dy
            if 0 <= nx < 1002 and 0<= ny < 1002:
                if arr[nx][ny] == 1e9:
                    visited[nx][ny] = visited[mx][my]
                    return visited[nx][ny]
                if arr[nx][ny] != -1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[mx][my] + 1

print(bfs(x, y))