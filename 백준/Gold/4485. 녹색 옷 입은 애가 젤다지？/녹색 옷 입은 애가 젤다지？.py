from collections import deque

tc = 1
while True:
    N = int(input())
    if N == 0:
        break

    rupee = [list(map(int, input().split())) for _ in range(N)]
    cost = [[1e9 for _ in range(N)] for _ in range(N)]

    queue = deque()
    queue.append((0, 0))
    cost[0][0] = rupee[0][0]

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if cost[nx][ny] > cost[x][y] + rupee[nx][ny]:
                    cost[nx][ny] = cost[x][y] + rupee[nx][ny]
                    queue.append((nx, ny))

    print(f'Problem {tc}: {cost[N - 1][N - 1]}')
    tc += 1