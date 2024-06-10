nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = list(A - B)
if ans:
    ans.sort()
    print(len(ans))
    print(*ans)
else:
    print(0)