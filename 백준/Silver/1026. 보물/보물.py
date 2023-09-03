import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(key=lambda x:-x)
B.sort()
S = 0
for i in range(N):
    S += A[i] * B[i]
print(S)