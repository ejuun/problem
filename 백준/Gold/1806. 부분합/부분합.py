N, S = map(int, input().split())
arr = list(map(int, input().split()))

length = 100000
end = 0
inter_sum = 0

for start in range(N):

    while inter_sum < S and end < N:
        inter_sum += arr[end]
        end += 1

    if inter_sum >= S:
        if length > (end - 1) - start + 1:
            length = (end - 1) - start + 1

    inter_sum -= arr[start]

if length == 100000:
    length = 0

print(length)