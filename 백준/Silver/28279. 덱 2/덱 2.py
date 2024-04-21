from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    od, *x = map(int, input().split())
    if od == 1:
        queue.appendleft(x[0])
    elif od == 2:
        queue.append(x[0])
    elif od == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif od == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif od == 5:
        print(len(queue))
    elif od == 6:
        if queue:
            print(0)
        else:
            print(1)
    elif od == 7:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif od == 8:
        if queue:
            print(queue[-1])
        else:
            print(-1)