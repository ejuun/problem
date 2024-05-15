import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]
ans = 0
hap = sum(A)
for i in range(N):
    hap -= A[i]
    ans += A[i] * hap
    
answer = ans % 1000000007
print(answer)