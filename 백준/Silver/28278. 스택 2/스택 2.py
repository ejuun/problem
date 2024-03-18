import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
stack = deque([])
for _ in range(N):
    order, *num = map(int, input().split())

    if order == 1:
        stack.append(num[0])
    elif order == 2:
        if stack:
            p = stack.pop()
            print(p)
        else:
            print(-1)
    elif order == 3:
        print(len(stack))
    elif order == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif order == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)