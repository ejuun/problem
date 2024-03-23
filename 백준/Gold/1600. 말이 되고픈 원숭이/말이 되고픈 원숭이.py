from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visited = [[[-1]*(K+1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 0

hdx = [-1, -2, -2, -1, 1, 2, 2, 1]
hdy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
queue.append((0, 0, 0))

while queue:
    x, y, cnt = queue.popleft()

    if cnt < K:
        for i in range(8):
            nhx = x + hdx[i]
            nhy = y + hdy[i]
            if 0 <= nhx < H and 0 <= nhy < W:
                if visited[nhx][nhy][cnt+1] == -1 and not arr[nhx][nhy]:
                    visited[nhx][nhy][cnt+1] = visited[x][y][cnt] + 1
                    queue.append((nhx, nhy, cnt+1))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W:
            if visited[nx][ny][cnt] == -1 and not arr[nx][ny]:
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                queue.append((nx, ny, cnt))

ans = 40001
for num in visited[-1][-1]:
    if num != -1 and ans > num :
       ans = num
if ans == 40001:
    ans = -1
print(ans)