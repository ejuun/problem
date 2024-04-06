from collections import deque
N, K = map(int, input().split())
visited = [100002] * 100001
queue = deque()
queue.append(N)
visited[N] = 0
ans = 0

if N == K:
    print(0)
    print(1)
else:
    while queue:
        x = queue.popleft()

        for dx in [x, -1, 1]:
            nx = x + dx
            if 0 <= nx < 100001:

                if nx == K:
                    if visited[nx] == 100002:
                        visited[nx] = visited[x] + 1
                        ans = 1
                    elif visited[x] + 1 == visited[K]:
                        ans += 1
                    continue

                if visited[nx] >= visited[x] + 1:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)

    print(visited[K])
    print(ans)