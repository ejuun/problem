from collections import deque
def solution(maps):
    answer = []
    queue = deque()
    visit = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j].isdigit() and not visit[i][j]:
                temp = 0
                queue.append((i, j))
                temp += int(maps[i][j])
                visit[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    
                    for dx, dy in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                            if maps[nx][ny] != 'X' and not visit[nx][ny]:
                                visit[nx][ny] = True
                                temp += int(maps[nx][ny])
                                queue.append((nx, ny))
                answer.append(temp)
    
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    return answer