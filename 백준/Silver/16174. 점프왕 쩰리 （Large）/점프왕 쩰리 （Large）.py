from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]

queue = deque()
visit[0][0] = True
queue.append((0, 0, arr[0][0]))

while queue:
    x, y, m = queue.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + m * dx
        ny = y + m * dy
        if 0 <= nx < N and 0 <= ny < N:
            if not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny, arr[nx][ny]))

if visit[-1][-1]:
    print("HaruHaru")
else:
    print("Hing")