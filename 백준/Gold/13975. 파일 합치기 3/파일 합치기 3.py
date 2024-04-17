from heapq import heappop, heappush
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    files = []
    K = int(input())
    arr = list(map(int, input().split()))

    for i in range(K):
        heappush(files, arr[i])

    ans = 0
    while len(files) != 1:
        file1 = heappop(files)
        file2 = heappop(files)
        new_file = file1 + file2
        ans += new_file
        heappush(files, new_file)

    print(ans)