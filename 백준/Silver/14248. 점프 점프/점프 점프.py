from collections import deque

n = int(input())
A = list(map(int, input().split()))
start = int(input()) - 1
visitid = [0] * n

queue = deque()
queue.append(start)
visitid[start] = 1

while queue:
    x = queue.popleft()

    for dx in [-A[x], A[x]]:
        nx = x + dx
        if 0 <= nx < n:
            if not visitid[nx]:
                queue.append(nx)
                visitid[nx] = 1
                
print(visitid.count(1))