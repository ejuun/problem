from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
queue = deque()
ans = [-1] * N

for i in range(N):
    while queue and queue[-1][0] < A[i]:
        tem, idx = queue.pop()
        ans[idx] = A[i]
    queue.append([A[i], i])

print(*ans)