import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)
arr.sort()

ans = []
for i in range(N):
    cnt = 0
    for j in range(arr[i], arr[i] + 5):
        if j not in arr:
            cnt += 1
    ans.append(cnt)
print(min(ans))