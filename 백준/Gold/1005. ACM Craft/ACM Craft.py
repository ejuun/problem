from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    bulid_time = [-1 for _ in range(N + 1)]

    order = [[i] for i in range(N + 1)]
    for _ in range(K):
        s, e = map(int, input().split())
        order[e].append(s)
    order.sort(key=lambda x: len(x))

    queue = deque(order)
    while queue:
        x = queue.popleft()

        if len(x) == 1:
            bulid_time[x[0]] = time[x[0]]
        else:
            able_time = -1
            for i in range(1, len(x)):
                if bulid_time[x[i]] == -1:
                    able_time = -1
                    queue.append(x)
                    break
                else:
                    if able_time < bulid_time[x[i]] + time[x[0]]:
                        able_time = bulid_time[x[i]] + time[x[0]]
            if able_time != -1:
              bulid_time[x[0]] = able_time
                
    W = int(input())
    print(bulid_time[W])