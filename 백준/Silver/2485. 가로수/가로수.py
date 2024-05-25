import math
import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
diff = []
for i in range(1, N):
    diff.append(arr[i] - arr[i-1])

gcd = math.gcd(diff[0], diff[1])
for i in range(2, len(diff)):
    gcd = math.gcd(gcd, diff[i])

ans = 0
for i in range(len(diff)):
    ans += diff[i] // gcd - 1
print(ans)