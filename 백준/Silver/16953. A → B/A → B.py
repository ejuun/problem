from collections import deque
A, B = map(int, input().split())
queue = deque()
cnt = 1
queue.append((A, cnt))
while 1:
    while queue:
        x, cnt = queue.popleft()

        if x == B:
            break

        for cal in [2*x, 10*x+1]:
            if cal <= B:
                queue.append((cal,cnt+1))
    if x == B:
        break

    if not queue:
        cnt = -1
        break

print(cnt)