import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
ans = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

for i in range(N):
    for j in range(N):
        if arr[i][j] != '.':
            ans[i][j] = '*'
        else:
            val = 0
            for k in range(8):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] != '.':
                        val += int(arr[ni][nj])
            if val >= 10:
                ans[i][j] = 'M'
            else:
                ans[i][j] = str(val)

for line in ans:
    print(''.join(line))