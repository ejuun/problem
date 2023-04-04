import sys

N = int(sys.stdin.readline())
stack = []
data = [sys.stdin.readline().rstrip() for _ in range(N)]

for word in data:
    if word[:4] == 'push':
        stack.append(word[5:])

    elif word[:3] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif word[:4] == 'size':
        print(len(stack))
    elif word[:5] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)