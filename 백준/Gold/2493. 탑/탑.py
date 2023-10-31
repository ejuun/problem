from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
stack = deque()
ans = [0] * (N+1)

for i in range(N, 0, -1):

    while stack and stack[-1][1] < arr[i]:
        idx, top = stack.pop()
        ans[idx] = i
    stack.append((i, arr[i]))

print(*ans[1:])