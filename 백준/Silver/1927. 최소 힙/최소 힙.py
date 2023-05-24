from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input())

arr = []

for _ in range(N):
    x = int(input())
    if x == 0 :
        if len(arr) == 0:
            print(0)
        else:
            print(heappop(arr))
    else:
        heappush(arr, x)