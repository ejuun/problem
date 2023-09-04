from collections import deque

queue = deque([i for i in range(1, int(input())+1)])

ans= []
while queue:
    card = queue.popleft()
    ans.append(card)
    queue.rotate(-1)
print(*ans)