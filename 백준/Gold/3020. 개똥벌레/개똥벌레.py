import sys
input = sys.stdin.readline
N, H = map(int, input().split())
arr = [0 for _ in range(H+1)]
front = [0 for _ in range(H+1)]
back = [0 for _ in range(H+1)]
for i in range(N):
    if i % 2:
        back[H - int(input()) + 1] += 1
    else:
        front[int(input())] += 1

for i in range(1, H+1):
    back[i] += back[i-1]

for i in range(H, 0, -1):
    front[i-1] += front[i]

for i in range(H+1):
    arr[i] = front[i] + back[i]

val = 200000
cnt = 0
for i in range(1, H+1):
    if arr[i] < val:
        val = arr[i]
        cnt = 1
    elif arr[i] == val:
        cnt += 1
        
print(val, cnt)