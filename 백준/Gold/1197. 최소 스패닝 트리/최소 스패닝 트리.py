def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

V, E = map(int, input().split())
p = [i for i in range(V + 1)]
G = []
for _ in range(E):
    A, B, C = map(int, input().split())
    G.append((A, B, C))
G.sort(key=lambda x: x[2])

cost = length = 0
for u, v, c in G:
    if find_set(u) != find_set(v):
        length += 1
        cost += c
        union(u, v)
        if length == V:
            break
print(cost)