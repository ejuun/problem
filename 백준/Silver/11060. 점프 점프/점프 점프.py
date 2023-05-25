from collections import deque

N = int(input())
arr = [0] + list(map(int, input().split()))
visited = [0] * (N + 1)
visited[1] = 1

def bfs():
    queue = deque()
    queue.append(1)
    if N == 1:
        return 1

    while queue:
        x = queue.popleft()

        if arr[x] == 0:
            continue
        for jump in range(1, arr[x] + 1):
            nx = x + jump
            if nx == N:
                visited[nx] = visited[x] + 1
                return visited[nx]
            if nx <= N:
                if not visited[nx]:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)
    return -1

ans = bfs()
if ans != -1:
    ans = ans -1
print(ans)