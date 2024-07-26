import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pay = [0 for _ in range(n)]
pay[0] = arr[0]
for i in range(1, n):
    pay[i] = pay[i-1] + arr[i]
pay = [0] + pay
ans = 0
for i in range(m, n+1):
    if ans < pay[i] - pay[i-m]:
        ans = pay[i] - pay[i-m]
print(ans)