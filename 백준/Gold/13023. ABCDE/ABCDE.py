import sys
sys.setrecursionlimit(2001)

def dfs(x, cnt):
    global ans

    if cnt == 5:
        ans = 1
        return

    for dot in G[x]:
        if not visited[dot]:
            visited[dot] = 1
            dfs(dot, cnt + 1)
            visited[dot] = 0

N, M = map(int, input().split())
G = [[] for _ in range(N)]
visited = [0] * N

for _ in range(M):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)
ans = 0

for i in range(N):
    dfs(i, 0)
    if ans:
        break

print(ans)