from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 외부 변환 시키기
air = deque()
air.append((0, 0))
arr[0][0] = 9
while air:
    x, y = air.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not arr[nx][ny]:
                arr[nx][ny] = 9
                air.append((nx, ny))
time = 0
while 1:
    time += 1
    # 2면이 닿아 있는 치즈 구하기
    disappear = set()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                side = 0
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 9:
                            side += 1
                if side >= 2:
                    disappear.add((i, j))
    # 구한 치즈 녹이기
    for x, y in disappear:
        arr[x][y] = 9

    # 공기와 맞닿아 있는 빈 부분 공기 채워주기
    hole = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 9:
                            hole.append((i, j))
                            arr[i][j] = 9
                            break

                while hole:

                    x, y = hole.popleft()

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if not arr[nx][ny]:
                                arr[nx][ny] = 9
                                hole.append((nx, ny))

    # 모두 녹아 없어졌는지 확인
    cheese = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cheese += 1
                break
        if cheese:
            break

    if not cheese:
        break

print(time)