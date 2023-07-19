N, M = map(int, input().split())
p = dict()

for i in range(1, N+1):
    pocketmon = input()
    p[pocketmon] = i
    p[i] = pocketmon

for _ in range(M):
    want = input()
    if not want.isdigit():
        print(p[want])
    else:
        print(p[int(want)])