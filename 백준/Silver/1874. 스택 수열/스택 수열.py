from collections import deque
n = int(input())
stack = deque()
ans = ''
i = 1
for _ in range(n):
    num = int(input())

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