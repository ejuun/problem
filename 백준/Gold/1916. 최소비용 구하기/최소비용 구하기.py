from heapq import heappush, heappop
N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
D = [1e9] * (N + 1)

for _ in range(M):
    s, e, weight = map(int, input().split())
    G[s].append((weight, e))

start, end = map(int, input().split())

D[start] = 0
q = [(0, start)]

while q:

    w, u = heappop(q)

    if D[u] < w:
        continue

    for w, v in G[u]:
        if D[v] > D[u] + w:
            D[v] = D[u] + w
            heappush(q, (D[v], v))

print(D[end])