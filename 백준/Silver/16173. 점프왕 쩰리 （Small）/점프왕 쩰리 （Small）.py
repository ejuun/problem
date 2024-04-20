from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]

visit[0][0] = True
queue = deque()
queue.append((0, 0, arr[0][0]))

while queue:
    x, y, move = queue.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + move * dx
        ny = y + move * dy
        if 0 <= nx < N and 0 <= ny < N:
            if not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny, arr[nx][ny]))

if not visit[-1][-1]:
    print('Hing')
else:
    print("HaruHaru")