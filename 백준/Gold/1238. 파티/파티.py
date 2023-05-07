from heapq import heappush, heappop
def cost(i, j):
    queue = []
    heappush(queue, i)
    visited = [1e7] * (N+1)
    visited[i] = 0

    while queue:
        x = heappop(queue)

        for p, time in G[x]:
            if visited[p] > visited[x] + time:
                visited[p] = visited[x] + time
                heappush(queue, p)

    return visited[j]

N, M, X = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, t = map(int, input().split())
    G[x].append((y, t))

ans = 0
for i in range(1, N+1):
    if i == X: continue
    if ans < cost(i, X) + cost(X, i):
        ans = cost(i, X) + cost(X, i)
print(ans)