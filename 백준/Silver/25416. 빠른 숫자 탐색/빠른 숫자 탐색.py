from collections import deque

def bfs(r, c, cnt):

    queue = deque()
    queue.append((r, c, cnt))
    visited[r][c] = 1
    while queue:
        x, y, c = queue.popleft()

        for dx, dy in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                if arr[nx][ny] == 1:
                    c += 1
                    return c

                if not arr[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny, c+1))
                    visited[nx][ny] = 1
    return -1

arr = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
visited = [[0 for _ in range(5)] for _ in range(5)]

print(bfs(r, c, 0))