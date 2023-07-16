from heapq import heappush, heappop
import sys
arr =[]

for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x:
        heappush(arr, -x)
    else:
        if len(arr):
            print(-heappop(arr))
        else:
            print(0)