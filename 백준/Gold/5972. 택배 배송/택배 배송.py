from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

INF = int(1e9)
ans = [INF] * (N + 1)
ans[1] = 0

queue = deque()
queue.append(1)
while queue:
    x = queue.popleft()

    for p, weight in G[x]:
        if ans[x] + weight < ans[p]:
            ans[p] = ans[x] + weight
            queue.append(p)

print(ans[N])