from collections import deque
def chain(i):
    queue = deque()
    queue.append(i)

    while queue:
        people = queue.popleft()
        for person in people:
            if not attention[person]:
                attention[person] = 1
                for k in range(M):
                    if person in parties[k]:
                        queue.append(parties[k])

N, M = map(int, input().split())

truth_num, *truth = map(int, input().split())
attention = [0] * (N+1)

if truth_num:
    for p in truth:
        attention[p] = 1

parties = []
for _ in range(M):
    p_num, *party = map(int, input().split())
    parties.append(party)

for i in range(1, N+1):
    for j in range(M):
        if attention[i] and i in parties[j]:
            chain(parties[j])

able = 0
for party in parties:
    stop = False
    for p in party:
        if attention[p]:
            stop = True
            break
    if stop == False:
        able += 1

print(able)