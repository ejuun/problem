import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = 0
S = dict()

for _ in range(N):
    word = input()
    S[word] = 1

for _ in range(M):
    check = input()
    if check in S.keys():
        ans += 1
print(ans)