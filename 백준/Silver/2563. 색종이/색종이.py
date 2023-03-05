N = int(input())

paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    sr, sc = map(int, input().split())

    re_sr = 100 - sc
    re_sc = sr

    for i in range(re_sr-9, re_sr+1):
        for j in range(re_sc, re_sc + 10):
            paper[i][j] = 1

cnt = 0
for line in paper:
    cnt += line.count(1)

print(cnt)