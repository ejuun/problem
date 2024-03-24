from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
        com, *num = map(str, input().split())
        if com == 'push':
                queue.append(int(num[0]))
        elif com == 'pop':
            if queue:
                x = queue.popleft();
                print(x)
            else:
                print(-1)
        elif com == 'size':
                print(len(queue))
        elif com == 'empty':
                if queue:
                        print(0)
                else:
                        print(1)
        elif com == 'front':
                if not queue:
                        print(-1)
                else:
                        print(queue[0])
        elif com == 'back':
                if not queue:
                        print(-1)
                else:
                        print(queue[-1])