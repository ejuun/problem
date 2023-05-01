from collections import deque

N, E = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

v1, v2 = map(int, input().split())
def load(i, j):
    visited = [1e9] * (N + 1)
    visited[i] = 0
    queue = deque()
    queue.append(i)

    while queue:
        x = queue.popleft()

        for p, weight in G[x]:
            if visited[p] > visited[x] + weight:
                visited[p] = visited[x] + weight
                queue.append(p)

    return visited[j]

a1 = load(1, v1)
b1 = load(v1, v2)
c1 = load(v2, N)

a2 = load(1, v2)
b2 = load(v2, v1)
c2 = load(v1, N)

ans = min(a1+b1+c1, a2+b2+c2)

if ans > 1e8:
    ans = -1
print(ans)