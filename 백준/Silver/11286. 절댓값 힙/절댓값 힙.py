from heapq import heappush, heappop
import  sys
N = int(sys.stdin.readline())
arr = []
real_num = []
for _ in range(N):
    num = int(sys.stdin.readline())

    if num:
        heappush(arr, abs(num))
        heappush(real_num, num)

    else:
        if len(arr):
            if -arr[0] in real_num:
                real_num.pop(real_num.index(-arr[0]))
                print(-heappop(arr))
            else:
                real_num.pop(real_num.index(arr[0]))
                print(heappop(arr))
        else:
            print(0)