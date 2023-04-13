from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[v].append(u)

max_cnt = 0

def bfs(i):
    global max_cnt
    visited = [0] * (N+1)
    queue = deque()
    queue.append(i)

    visited[i] = 1

    while queue:
        x = queue.popleft()

        for w in G[x]:
            if not visited[w]:
                visited[w] = 1
                queue.append(w)

    if max_cnt <= visited.count(1):
        max_cnt = visited.count(1)

    return visited.count(1)

ans =[0] * (N+1)
for i in range(1, N+1):
    ans[i] = bfs(i)
for i in range(1, N+1):
    if max_cnt == ans[i]:
        print(i, end=' ')