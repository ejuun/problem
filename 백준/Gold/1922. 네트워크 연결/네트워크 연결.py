def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

N = int(input())
M = int(input())
p = [i for i in range(N + 1)]
G = []

for _ in range(M):
    a, b, c = map(int, input().split())
    G.append([a, b, c])

G.sort(key=lambda x: x[2])

s = 0
cnt = 0

for u, v, weight in G:
    if find_set(u) != find_set(v):
        cnt += 1
        s += weight
        union(u, v)
        if cnt == N:
            break

print(s)