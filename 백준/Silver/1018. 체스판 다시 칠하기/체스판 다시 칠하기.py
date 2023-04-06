def check(i, j):
    cnt = 0
    for k in range(i, i + 8, 2):
        for l in range(j, j + 8, 2):
            if board[k][l] != board[i][j]:
                cnt += 1

        for l in range(j + 1, j + 8, 2):
            if board[k][l] == board[i][j]:
                cnt += 1

    for k in range(i + 1, i + 8, 2):
        for l in range(j, j + 8, 2):
            if board[k][l] == board[i][j]:
                cnt += 1
        for l in range(j + 1, j + 8, 2):
            if board[k][l] != board[i][j]:
                cnt += 1
    return cnt

N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]

min_val = 1e9
for i in range(N-8+1):
    for j in range(M-8+1):
        if board[i][j] == 'W':
            cnt = check(i,j)
            board[i][j] = 'B'
            cnt_change = check(i,j) + 1
            board[i][j] = 'W'
        else:
            cnt = check(i,j)
            board[i][j] = 'W'
            cnt_change = check(i,j) + 1
            board[i][j] = 'B'

        if min_val > min(cnt, cnt_change):
            min_val = min(cnt, cnt_change)

print(min_val)
