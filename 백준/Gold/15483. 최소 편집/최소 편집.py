A = '=' + input()
B = '-' + input()
arr = [[0 for _ in range(len(B))] for _ in range(len(A))]

for i in range(len(A)):
    arr[i][0] = i
for j in range(len(B)):
    arr[0][j] = j

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            arr[i][j] = arr[i-1][j-1]
        else:
            arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1

print(arr[-1][-1])