from collections import deque

N, K = map(int, input().split())
visited = [0] * 100002

queue = deque()
queue.append(N)
visited[N] = 1

while queue:
    x = queue.popleft()

    if x == K:
        break

    for dir in [x, -1, 1]:
        nx = x + dir
        if 0 <= nx <= 100001 and not visited[nx]:
            queue.append(nx)
            if dir == x:
                visited[nx] = visited[x]
            else:
                visited[nx] = visited[x] + 1
                
if not visited[K]:
    print(visited[K])
else:
    print(visited[K]-1)