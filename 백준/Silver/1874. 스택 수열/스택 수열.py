from collections import deque
import sys

n = int(sys.stdin.readline())
stack = deque()
ans = ''
i = 1
for _ in range(n):
    num = int(sys.stdin.readline())

    while i <= num:
        stack.append(i)
        ans += '+\n'
        i += 1

    if stack[-1] == num:
        stack.pop()
        ans += '-\n'

    else:
        ans = 'NO'
        break

print(ans)