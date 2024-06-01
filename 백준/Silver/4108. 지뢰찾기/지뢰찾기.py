while 1:
    R, C = map(int, input().split())
    if not R and not C:
        break

    lst = [list(map(str, input())) for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if lst[i][j] == '.':
                lst[i][j] = 0
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        if lst[ni][nj] == '*':
                            lst[i][j] += 1
                lst[i][j] = str(lst[i][j])
                
    for line in lst:
        print(''.join(line))