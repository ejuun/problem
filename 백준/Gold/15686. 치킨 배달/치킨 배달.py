from collections import deque
import itertools

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append((i, j))
        if arr[i][j] == 1:
            house += 1

able = itertools.combinations(chicken, M)

min_dis = 1e9
for ab in able:
    dis = 0
    cnt = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    
    for a in ab:
        queue.append(a)
        visited[a[0]][a[1]] = 1
        
    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    if arr[nx][ny] == 1:
                        cnt += 1
                        dis += visited[nx][ny] - 1
                        if cnt == house:
                            break
                    queue.append((nx, ny))

        if cnt == house:
            break
    if min_dis > dis:
        min_dis = dis

print(min_dis)