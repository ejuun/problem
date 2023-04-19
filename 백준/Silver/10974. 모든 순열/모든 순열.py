def back(i):
    if i == N:
        ans.append(arr[:])

    for j in range(i, N):
        arr[i], arr[j] = arr[j], arr[i]
        back(i + 1)
        arr[i], arr[j] = arr[j], arr[i]

N = int(input())
arr = [i for i in range(1, N + 1)]
ans = []

back(0)

ans.sort()
for lst in ans:
    print(*lst)