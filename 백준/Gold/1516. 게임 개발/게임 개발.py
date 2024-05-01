from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = []
time = [0 for _ in range(N+1)]

for i in range(1, N+1):
    build = [i] + list(map(int, input().split()))
    build.pop()
    arr.append(build)
arr.sort(key=lambda x : len(x))

queue = deque(arr)
while queue:
    cmd = queue.popleft()

    if len(cmd) == 2:
        time[cmd[0]] = cmd[1]
    else:
        temp = 0
        for i in range(2, len(cmd)):
            if time[cmd[i]]:
                if temp < time[cmd[i]]:
                    temp = time[cmd[i]]
            else:
                temp = 0
                break
        if not temp:
            queue.append(cmd)
        else:
            time[cmd[0]] = cmd[1] + temp
            
for i in range(1, len(time)):
    print(time[i])