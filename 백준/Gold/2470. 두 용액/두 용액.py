N = int(input())
arr = list(map(int, input().split()))
arr.sort()
mixed = 2000000000
end = N-1
start = small = large = 0

while start < end:
    hap = arr[start] + arr[end]

    if abs(hap) < mixed:
        mixed = abs(hap)
        small = arr[start]
        large = arr[end]

        if hap == 0:
            break

    if hap < 0:
        start += 1
    else:
        end -= 1

print(small, large)