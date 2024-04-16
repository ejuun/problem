from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
order = [0 for _ in range(N+1)]
pre = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    pre[B] += 1

queue = deque()
for i in range(1, N+1):
    if not pre[i]:
        queue.append((i, 1))

while queue:
    x, cnt = queue.popleft()
    order[x] = cnt

    for c in G[x]:
        pre[c] -= 1
        if not pre[c]:
            queue.append((c, cnt+1))

print(*order[1:])