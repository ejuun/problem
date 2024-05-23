N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
ans = [0, 0]

for i in range(N):
    row = 0
    for j in range(N):
        if arr[i][j] == '.':
            row += 1
        else:
            row = 0
        if row == 2:
            ans[0] += 1

    col = 0
    for j in range(N):
        if arr[j][i] == '.':
           col += 1
        else:
            col = 0
        if col == 2:
            ans[1] += 1

print(*ans)