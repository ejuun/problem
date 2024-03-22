from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

queue =deque()
queue.append(R)

visited = [-1 for _ in range(N+1)]
visited[R] = 0

while queue:
    x = queue.popleft()

    for num in G[x]:
        if visited[num] == -1:
            visited[num] = visited[x] + 1
            queue.append(num)

for i in range(1, len(visited)):
    print(visited[i])