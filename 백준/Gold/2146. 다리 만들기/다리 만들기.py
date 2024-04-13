from collections import deque
import sys
input = sys.stdin.readline

def land(i, j, l):
    queue = deque()
    queue.append((i, j))
    sep[i][j] = l

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] and not sep[nx][ny]:
                    sep[nx][ny] = sep[x][y]
                    queue.append((nx, ny))

def bridge(i, j, l):
    queue = deque()
    queue.append((i, j))
    visit = [[0 for _ in range(N)] for _ in range(N)]
    visit[i][j] = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] and sep[nx][ny] != l:
                    return visit[x][y] - 1
                elif not sep[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))
    return 10001

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sep = [[0 for _ in range(N)] for _ in range(N)]
l = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        if arr[i][j] and not sep[i][j]:
            land(i, j, l)
            l -= 1

ans = 10001
for i in range(N):
    for j in range(N):
        if l < sep[i][j] < 0:
            ans = min(ans, bridge(i, j, sep[i][j]))

print(ans)