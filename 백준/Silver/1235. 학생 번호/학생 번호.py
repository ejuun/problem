N = int(input())
arr = []
for _ in range(N):
    arr.append(input())

l = len(arr[0])
ans = 0
for i in range(l, -1, -1):
    ans += 1
    length = set()
    for j in range(N):
        length.add(arr[j][i-1:])
    if len(length) == N:
        break
print(ans)