l1 = '=' + input()
l2 = '-' + input()
l3 = '.' + input()

arr = [[[0 for _ in range(len(l3))] for _ in range(len(l2))] for _ in range(len(l1))]

for i in range(len(l1)):
    for j in range(len(l2)):
        for k in range(len(l3)):
            if i == 0 or j == 0 or k == 0:
                continue
            if l1[i] == l2[j] == l3[k]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            else:
                arr[i][j][k] = max(arr[i-1][j][k], arr[i][j-1][k], arr[i][j][k-1])

print(arr[-1][-1][-1])