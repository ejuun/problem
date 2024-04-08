H, W = map(int, input().split())
lst = list(map(int, input().split()))
rain = [[0 for _ in range(W)] for _ in range(H)]
for i in range(len(lst)):
    for j in range(lst[i]):
        rain[j][i] = 1

ans = 0
for i in range(H):
    wall = check = 0
    for j in range(W):
        if rain[i][j]:
            wall += 1
            if wall == 2:
                if check:
                    ans += check
                    check = 0
                wall = 1
        else:
            if wall == 1:
                check += 1
print(ans)