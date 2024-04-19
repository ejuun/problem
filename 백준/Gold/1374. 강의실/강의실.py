from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    n, s, e = map(int, input().split())
    time.append((s, e))

time.sort(key=lambda x: (x[0], x[1]))
clas = []
heappush(clas, time[0][1])

for i in range(1, N):
    if clas[0] <= time[i][0]:
        heappop(clas)
    heappush(clas, time[i][1])

print(len(clas))