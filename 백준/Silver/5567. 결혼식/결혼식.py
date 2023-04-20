from collections import deque

n = int(input())
m = int(input())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

queue = deque()
queue.append(1)

visited = [0] * (n+1)
visited[1] = 1

while queue:
    x = queue.popleft()

    for friend in G[x]:
        if not visited[friend]:
            queue.append(friend)
            visited[friend] = visited[x] + 1

ans = 0
for f in visited:
    if f == 2 or f == 3:
       ans += 1

print(ans)