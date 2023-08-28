import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * (N+1)
if N == 0:
    print(0)
else:
    arr[1] = 1
    for i in range(2, N+1):
        arr[i] = (arr[i-1] + arr[i-2]) % 1000000007
    print(arr[N])