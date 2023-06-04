import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    if x < y:
        p[find_set(y)] = find_set(x)
    elif x > y:
        p[find_set(x)] = find_set(y)

n, m = map(int, input().split())

p = [i for i in range(n+1)]

for _ in range(m):
    put, a, b = map(int, input().split())

    if put == 0:
        union(a, b)
    else:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')

