import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(R)]
sets = set()
sets.add(arr[0][0])
move = 0

def dfs(x, y, cnt):
    global move
    move = max(cnt, move)

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if arr[nx][ny] not in sets:
                sets.add(arr[nx][ny])
                dfs(nx, ny, cnt + 1)
                sets.remove(arr[nx][ny])

dfs(0, 0, 1)
print(move)