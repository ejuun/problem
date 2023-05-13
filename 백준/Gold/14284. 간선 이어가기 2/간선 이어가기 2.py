from collections import deque

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    G[a].append((b, c))
    G[b].append((a, c))

s, t = map(int, input().split())

visited = [1e8] * (n+1)
visited[s] = 0

queue = deque()
queue.append(s)

while queue:
    x = queue.popleft()

    for p, c in G[x]:
        if visited[p] > visited[x] + c:
            visited[p] = visited[x] + c
            queue.append(p)

print(visited[t])