N, M = map(int, input().split())
arr = [0] * N

for i in range(N):
    arr[i] = int(input())
arr.sort()

end = 0
ans = 1e10+1
for start in range(len(arr)):

    while end < N:
        diff = arr[end] - arr[start]
        if diff >= M:
            if diff < ans:
                ans = diff
            break
        else:
            end += 1
print(ans)