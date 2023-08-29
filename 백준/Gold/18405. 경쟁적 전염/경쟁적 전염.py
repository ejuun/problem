import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

def spread(n_spot):
    for x, y, n in n_spot:
        for dx, dy in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not arr[nx][ny]:
                    arr[nx][ny] = n
time = 0
ans = 0

if S == 0:
    print(arr[X-1][Y-1])
else:
    while time < S:

        for n in range(1, K+1):
            n_spot = []
            for i in range(N):
                for j in range(N):
                    if arr[i][j] == n:
                        n_spot.append((i, j, n))

            spread(n_spot)

        if arr[X-1][Y-1]:
            ans = arr[X-1][Y-1]
            break
        time += 1

    print(ans)