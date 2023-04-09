from collections import deque

N, K = map(int, input().split())

visited = [0] * 100001

queue = deque()
queue.append(N)

cnt = 1
visited[N] = cnt
cycle_visited = []

while not visited[K]:

    for q in cycle_visited:
        queue.append(q)

    cycle_visited.clear()

    cnt += 1

    while queue:
        n = queue.popleft()

        dx = [-1, 1, n]

        for dir in range(3):
            new_N = n + dx[dir]
            if 0 <= new_N <= 100000:
                if not visited[new_N]:
                    visited[new_N] = cnt
                    cycle_visited.append(new_N)
                if new_N == K:
                    break
        if visited[K]:
            break

if N == K:
    print(0)
else:
    print(visited[K]-1)
