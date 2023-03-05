N = int(input())
paper = [[0 for _ in range(1001)] for _ in range(1001)]
for cnt in range(1, N+1):
    sc, sr, w, h = map(int, input().split())

    for i in range(sr, sr+h):
        for j in range(sc, sc+w):
            paper[i][j] = cnt

for cnt in range(1, N+1):
    total = 0
    for line in paper:
        total += line.count(cnt)

    print(total)