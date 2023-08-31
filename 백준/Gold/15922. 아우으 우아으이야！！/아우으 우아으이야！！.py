import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append((s, e))

start = arr[0][0]
end = arr[0][1]
ans = end - start

for ls, le in arr:
    if le > end:
        if ls <= end:
            ans += le - end
            end = le
        else:
            start = ls
            end = le
            ans += end - start
print(ans)