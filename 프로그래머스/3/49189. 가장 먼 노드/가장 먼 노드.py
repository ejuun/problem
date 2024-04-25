from collections import deque

def solution(n, edge):
    answer = 0
    G = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    for node in edge:
        G[node[0]].append(node[1])
        G[node[1]].append(node[0])
    queue = deque()
    queue.append(1)
    visit[1] = 1
    while queue:
        x = queue.popleft()
        
        for dot in G[x]:
            if not visit[dot]:
                visit[dot] = visit[x] + 1
                queue.append(dot)
                
    max_val = 0
    for i in range(len(visit)):
        if max_val == visit[i]:
            answer += 1
            
        if max_val < visit[i]:
            max_val = visit[i]
            answer = 1

    return answer