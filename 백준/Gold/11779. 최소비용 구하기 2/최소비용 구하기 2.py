from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
G = [{} for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    if v not in G[u] or G[u][v] > w:
        G[u][v] = w

start, end = map(int, input().split())

queue = []
heappush(queue, start)

visited = [1e9] * (n+1)
visited[start] = 0

move = [0] * (n+1)

while queue:
    x = heappop(queue)

    for p in G[x]:
        cost = G[x][p]
        if visited[p] > visited[x] + cost:
            visited[p] = visited[x] + cost
            heappush(queue, p)
            move[p] = x

i = end
ans = [i]
while move[i] != 0:
    ans.append(move[i])
    i = move[i]

ans.reverse()

print(visited[end])
print(len(ans))
print(*ans)