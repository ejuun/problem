import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
start = 0
end = N-1

while start < end:
    armor = arr[start] + arr[end]

    if armor > M:
        end -=1
    elif armor < M:
        start += 1
    else:
        ans += 1
        start +=1
        end -=1

print(ans)