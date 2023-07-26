k1 = '+' + input()
k2 = '-' + input()
lk1 = len(k1)
lk2 = len(k2)

arr = [[0 for _ in range(lk2)] for _ in range(lk1)]

for i in range(lk1):
    for j in range(lk2):
        if i == 0 or j == 0:
            continue
        if k1[i] == k2[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(arr[lk1-1][lk2-1])