from heapq import heappush, heappop

def least(i):
    visited = [INF] * (N + 1)
    queue = []
    heappush(queue, i)
    visited[i] = 0

    while queue:
        x = heappop(queue)

        for p, len in G[x]:
            if visited[p] > visited[x] + len:
                visited[p] = visited[x] + len
                heappush(queue, p)
    return visited

for _ in range(int(input())):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a].append((b, c))
        G[b].append((a, c))

    K = int(input())
    friends = list(map(int, input().split()))

    INF = 100001
    ans = 0
    min_len = INF
    ans = [0] * (N+1)
    for i in range(K):
        able = least(friends[i])
        for j in range(len(ans)):
            ans[j] += able[j]

    print(ans.index((min(ans))))