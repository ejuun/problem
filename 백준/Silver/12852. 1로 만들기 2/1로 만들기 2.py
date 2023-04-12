from collections import deque

N = int(input())
visited = [0] * (N+1)
cnt = 0

queue = deque()
queue.append((N, cnt))

while queue:
    x, cnt = queue.popleft()

    if x == 1:
        break

    for div in [3, 2]:
        if not(x % div):
            new_x = x // div

            if not visited[new_x]:
                new_cnt = cnt + 1
                queue.append((new_x, new_cnt))
                visited[new_x] = x

    new_x = x - 1
    if not visited[new_x]:
        new_cnt = cnt + 1
        queue.append((new_x, new_cnt))
        visited[new_x] = x


temp = 1
ans = [1]
while temp != N:
    ans.append(visited[temp])
    temp = visited[temp]

print(cnt)
print(*ans[::-1])
