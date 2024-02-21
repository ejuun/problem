import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split())) + [0]

l = 1
ans = 0
for i in range(0, len(arr)-1):
    if arr[i] < arr[i+1]:
        l += 1
    else:
        if l > 1:
            ans += int((l * (l+1) / 2))
        else:
            ans += 1
        l = 1
print(ans)