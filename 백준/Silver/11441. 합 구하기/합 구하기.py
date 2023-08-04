import sys

N = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
hap = [0] * (N+1)
for i in range(1, N+1):
    hap[i] = hap[i-1] + num[i]

M = int(sys.stdin.readline())
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(hap[end] - hap[start-1])