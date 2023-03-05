N = int(input())

paper = [[0 for _ in range(102)] for _ in range(102)]

for _ in range(N):
    c, r = map(int, input().split())

    for i in range(r, r+10):
        for j in range(c, c+10):
            paper[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #상 하 좌 우

cnt  = 0
for i in range(102):
    for j in range(102):
        if paper[i][j]:
            for dir in range(4):
                ni = i + dx[dir]
                nj = j + dy[dir]
                if 0 <= ni < 102 and 0 <= nj < 102:
                    if not paper[ni][nj]:
                        cnt += 1
print(cnt)