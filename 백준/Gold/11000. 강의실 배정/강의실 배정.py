from heapq import heappop, heappush
import sys
input = sys.stdin.readline
arr = []
N = int(input())
for _ in range(N):
   arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[0], x[1]))

cls = [arr[0][1]]
for i in range(1, N):
    if cls[0] <= arr[i][0]:
        heappop(cls)
    heappush(cls, arr[i][1])

print(len(cls))