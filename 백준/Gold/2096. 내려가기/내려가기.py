N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mini = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
    for j in range(3):
        mini[i][j] = arr[i][j]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            arr[i][j] += max(arr[i-1][j], arr[i-1][j+1])
        elif j == 1:
            arr[i][j] += max(arr[i-1][j-1], arr[i - 1][j], arr[i - 1][j + 1])
        else:
            arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])

for i in range(1, N):
    for j in range(3):
        if j == 0:
            mini[i][j] += min(mini[i - 1][j], mini[i - 1][j + 1])
        elif j == 1:
            mini[i][j] += min(mini[i - 1][j - 1], mini[i - 1][j], mini[i - 1][j + 1])
        else:
            mini[i][j] += min(mini[i - 1][j - 1], mini[i - 1][j])

print(max(arr[N-1]), min(mini[N-1]))