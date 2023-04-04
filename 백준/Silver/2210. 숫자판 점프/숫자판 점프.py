
m = [list(map(int, input().split())) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
check = set()

def back(i, j):
    if len(arr) == 6:
        check.add(tuple(arr))
        return

    for dir in range(4):
        ni = i + dx[dir]
        nj = j + dy[dir]
        if 0 <= ni < 5 and 0 <= nj < 5:
            arr.append(m[ni][nj])
            back(ni, nj)
            arr.pop()
    return


for i in range(5):
    for j in range(5):
        arr = [m[i][j]]
        back(i, j)

print(len(check))