N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N-1
hap = 200000001
mix = 0

while start < end:

    mix = arr[start] + arr[end]

    if abs(mix) < abs(hap):
        hap = mix

    if hap == 0:
        break

    if mix < 0 :
        start += 1
    else:
        end -= 1

print(hap)