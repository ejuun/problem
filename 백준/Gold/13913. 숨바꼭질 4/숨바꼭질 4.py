from collections import deque
N, K = map(int, input().split())
visited = [0] * 100001
checked = [0] * 100001
lst = [N]

check = 0

queue = deque()
queue.append(N)
visited[N] = 1

while queue:
    x = queue.popleft()

    if x == K:
        break

    for dir in [-1, 1, x]:
        nx = x + dir
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = visited[x] + 1
            checked[nx] = x
            queue.append(nx)
            if nx == K:
                check = 1
                break
    if check:
        break

ans = [K]
temp = K
while temp != N:
    ans.append(checked[temp])
    temp = checked[temp]
ans.reverse()

print(visited[K]-1)
print(*ans)