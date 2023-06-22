l1 = '-' + input()
l2 = '=' + input()

len_l1 = len(l1)
len_l2 = len(l2)

check = [[0 for _ in range(len_l2)] for _ in range(len_l1)]

for i in range(len_l1):
    for j in range(len_l2):
        if i and j:
            if l1[i] == l2[j]:
                check[i][j] = check[i-1][j-1] + 1
            else:
                check[i][j] = max(check[i-1][j], check[i][j-1])

ans = check[-1][-1]
if ans:
    i = len(l1)-1
    j = len(l2)-1
    lcs = ''

    while ans:
        if check[i][j] != check[i-1][j] and check[i][j] != check[i][j-1]:
            lcs += l1[i]
            i -= 1
            j -= 1
            ans -= 1
        elif check[i][j] == check[i-1][j]:
            i -= 1
        elif check[i][j] == check[i][j-1]:
            j -= 1

    print(check[-1][-1])
    print(lcs[::-1])
else:
    print(0)