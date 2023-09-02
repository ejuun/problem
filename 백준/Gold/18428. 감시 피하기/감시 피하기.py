import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
teachers = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            teachers.append((i, j))

ans = False

def check():
    global arr
    for x, y in teachers:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            for n in range(1, N):
                nx = x + n * dx
                ny = y + n * dy
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] == 'O':
                        break
                    elif arr[nx][ny] == 'S':
                        return True
    return False

def back(cnt):
    global ans

    if cnt == 3:
        if check() == False:
            ans = True
            return
    else:
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'X':
                    arr[i][j] = 'O'
                    back(cnt + 1)
                    arr[i][j] = 'X'
back(0)

if ans:
    print('YES')
else:
    print('NO')