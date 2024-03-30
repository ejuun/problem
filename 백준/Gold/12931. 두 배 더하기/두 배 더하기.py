N = int(input())
arr = list(map(int, input().split()))
zero = set()
ans = 0

while len(zero) < N:

    odd = 0
    for i in range(N):
        if not arr[i]:
            zero.add(i)
        elif arr[i] % 2:
            arr[i] -= 1
            ans += 1
            odd = 1

    if len(zero) == N:
        break

    if not odd:
        for i in range(N):
            arr[i] = arr[i] // 2
        ans += 1
        
print(ans)