l1 = '_' + input()
l2 = ')' + input()

arr = [[0 for _ in range(len(l2))] for _ in range(len(l1))]

for i in range(len(l1)):
    for j in range(len(l2)):
        if i == 0 or j == 0:
            continue
        if l1[i] == l2[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

ans = arr[-1][-1]
if ans:
    i = len(l1)-1
    j = len(l2)-1
    lcs = ''

    while ans:
        if arr[i][j] != arr[i-1][j] and arr[i][j] != arr[i][j-1]:
            lcs += l1[i]
            i -= 1
            j -= 1
            ans -= 1
        elif arr[i][j] == arr[i-1][j]:
            i -= 1
        elif arr[i][j] == arr[i][j-1]:
            j -= 1
    print(lcs[::-1])