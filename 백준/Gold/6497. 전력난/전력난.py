def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

while 1:
    m, n = map(int, input().split())
    if not m and not n:
        break

    p = [i for i in range(m + 1)]
    G = []
    total = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        total += z
        G.append((x, y, z))

    G.sort(key=lambda x: x[2])

    len = cost = 0
    for l1, l2, c in G:
        if find_set(l1) != find_set(l2):
            len += 1
            cost += c
            union(l1, l2)
            if len == m:
                break

    ans = total - cost
    print(ans)