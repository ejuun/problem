from collections import deque

def bfs(S, T, cnt):
    queue = deque()
    queue.append((S, T, cnt))

    while queue:
        s, t, c = queue.popleft()

        for ds, dt in [(s, 3), (1, 0)]:
            ns = s + ds
            nt = t + dt
            if ns > nt:
                continue
            if ns == nt:
                return c
            else:
                queue.append((ns, nt, c + 1))

C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    print(bfs(S, T, 1))