import sys
input = sys.stdin.readline

def bi(arr, num):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < num:
            l = m + 1
        else:
            r = m - 1
    return l

N = int(input())
A = list(map(int, input().split()))

val = [A[0]]
for i in range(1, N):
    if val[-1] < A[i]:
        val.append(A[i])
    else:
        idx = bi(val, A[i])
        val[idx] = A[i]

print(len(val))