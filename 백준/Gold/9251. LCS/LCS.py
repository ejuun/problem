line1 = '.' + input()
line2 = '`' + input()
lcs = [[0 for _ in range(len(line2))] for _ in range(len(line1))]

for i in range(len(line1)):
    for j in range(len(line2)):
        if i == 0 or j == 0:
            lcs[i][j] == 0
        elif line1[i] == line2[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[-1][-1])