from collections import deque

def bfs(queue, visit):
    while queue:
        x, y, z = queue.popleft()

        if arr[x][y][z] == 'E':
            return 'Escaped in {} minute(s).'.format(visit[x][y][z]-1)

        for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if arr[nx][ny][nz] != '#' and not visit[nx][ny][nz]:
                    visit[nx][ny][nz] = visit[x][y][z] + 1
                    queue.append((nx, ny, nz))

    return 'Trapped!'

def find_S():
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    queue.append((i, j, k))
                    visit[i][j][k] = 1
                    return

while 1:
    L, R, C = map(int, input().split())
    if not L and not R and not C:
        break

    arr = [[list(map(str, input())) for _ in range(R + 1)] for _ in range(L)]
    visit = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    queue = deque()
    find_S()
    print(bfs(queue, visit))