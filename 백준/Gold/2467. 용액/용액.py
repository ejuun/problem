N = int(input())
liquid = list(map(int, input().split()))

ans = 2000000000
start = 0
end = N-1
small = large = 0

while start < end:
    hap = liquid[start] + liquid[end]

    if abs(hap) <= ans:
        small = liquid[start]
        large = liquid[end]
        ans = abs(hap)

        if ans == 0:
            break

    if hap < 0:
        start += 1
    else:
        end -= 1

print(small, large)