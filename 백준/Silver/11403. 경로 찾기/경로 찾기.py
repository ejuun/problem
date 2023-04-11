from collections import deque
def bfs(i):
    queue =deque()
    queue.append(i)
    visited = [0] * (N)
    while queue:
        x = queue.popleft()

        for w in G[x]:
            if not visited[w]:
                visited[w] = 1
                queue.append(w)
    return visited

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
G = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if adj[i][j]:
            G[i].append(j)

for i in range(N):
    print(*bfs(i))