DDuk = [[0, 0] for _ in range(31)]
DDuk[1] = [1, 0]
DDuk[2] = [0, 1]

D, K = map(int, input().split())

for i in range(3, D + 1):
    DDuk[i][0] = DDuk[i - 2][0] + DDuk[i - 1][0]
    DDuk[i][1] = DDuk[i - 2][1] + DDuk[i - 1][1]

i = j = 1
while 1:
    if DDuk[D][0] * i + DDuk[D][1] * j == K:
        break
    else:
        j += 1
        if DDuk[D][0] * i + DDuk[D][1] * j > K:
            i += 1
            j = 1
print(i)
print(j)