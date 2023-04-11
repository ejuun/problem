from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

def bfs(i):
    visited = [0] * (N+1)
    queue = deque()
    queue.append(i)
    visited[i] = 1

    while queue:
        x = queue.popleft()

        for w in G[x]:
            if not visited[w]:
                visited[w] += visited[x] + 1
                queue.append(w)
    return visited

able = []
for i in range(1, N+1):
    kevin = bfs(i)
    able.append(sum(kevin))
print(able.index(min(able))+1)