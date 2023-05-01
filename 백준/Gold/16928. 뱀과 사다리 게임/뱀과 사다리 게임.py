from collections import deque

N, M = map(int, input().split())
ladder = dict()
snake = dict()
for _ in range(N):
    s, e = map(int, input().split())
    ladder[s] = e
for _ in range(M):
    s, e = map(int, input().split())
    snake[s] = e

def move(cnt):
    visited = [0] * 101
    visited[1] = cnt + 1
    queue = deque()
    queue.append((1, cnt+1))

    while queue:
        point, move_cnt = queue.popleft()

        for dice in [1, 2, 3, 4, 5, 6]:
            new_point = point + dice
            if new_point < 101:
                if not visited[new_point] or move_cnt + 1 < visited[new_point]:
                    if new_point == 100:
                        visited[new_point] = move_cnt
                        return visited[100]

                    if new_point in ladder:
                        visited[ladder[new_point]] = move_cnt + 1
                        queue.append((ladder[new_point], move_cnt + 1))
                    elif new_point in snake:
                        visited[snake[new_point]] = move_cnt + 1
                        queue.append((snake[new_point], move_cnt + 1))
                    else:
                        visited[new_point] = move_cnt + 1
                        queue.append((new_point, move_cnt + 1))

print(move(0))