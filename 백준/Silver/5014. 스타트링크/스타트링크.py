from collections import deque

F, S, G, U, D = map(int, input().split())
buliding = [-1] * (F + 1)

def bfs(F, S, G, U, D):
    queue = deque()
    queue.append(S)
    buliding[S] = 1

    if S == G:
        buliding[G] = 0
        return buliding[G]

    while queue:
        stay = queue.popleft()

        for new in [stay + U, stay - D]:
            if 0 < new <= F:
                if new == G:
                    buliding[new] = buliding[stay]
                    return buliding[G]
                if buliding[new] == -1:
                    buliding[new] = buliding[stay] + 1
                    queue.append(new)

    return buliding[G]

ans = bfs(F, S, G, U, D)
if ans == -1:
    ans = 'use the stairs'
print(ans)