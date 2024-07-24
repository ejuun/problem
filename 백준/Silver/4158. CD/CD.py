
while 1:
    ans = 0
    dic = {}
    N, M = map(int, input().split())
    if not N and not M:
        break

    for _ in range(N):
        n = int(input())
        dic[n] = 0

    for _ in range(M):
        m = int(input())
        if m in dic:
            ans += 1
    print(ans)