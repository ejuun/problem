def fac(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * fac(N-1)

for tc in range(int(input())):
    N, M = map(int, input().split())

    ans = fac(M) // (fac(N) * fac((M-N)))

    print(ans)