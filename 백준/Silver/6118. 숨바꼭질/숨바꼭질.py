from collections import deque
N, M = map(int, input().split())

G = [set() for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u].add(v)
    G[v].add(u)
visited = [0] * (N+1)
visited[1] = 1
queue = deque()
queue.append(1)

while queue:
    x = queue.popleft()

    for p in G[x]:
        if not visited[p]:
            visited[p] = visited[x] + 1
            queue.append(p)

max_len = max(visited)-1
max_cnt = visited.count(max(visited))

print(visited.index(max(visited)), max_len, max_cnt)