from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
crush = [[2500 for _ in range(n)] for _ in range(n)]

queue = deque()
queue.append((0, 0, 0))

while queue:
    x, y, c = queue.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if not arr[nx][ny]:
               if crush[nx][ny] > c + 1:
                   crush[nx][ny] = c + 1
                   queue.append((nx, ny, c+1))

            else:
                if crush[nx][ny] > c:
                    crush[nx][ny] = c
                    queue.append((nx, ny, c))

print(crush[n-1][n-1])