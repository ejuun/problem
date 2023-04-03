from collections import deque
queue = deque([i for i in range(1, int(input())+1)])

while len(queue)!= 1:
    queue.popleft()
    queue.rotate(-1)

print(*queue)