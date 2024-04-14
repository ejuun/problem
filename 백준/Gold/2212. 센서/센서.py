import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(set(list(map(int, input().split()))))
arr.sort()

diff = []
for i in range(1, len(arr)):
    diff.append(arr[i]-arr[i-1])
diff.sort()

ans = 0
for i in range(len(diff)-K+1):
    ans += diff[i]
print(ans)