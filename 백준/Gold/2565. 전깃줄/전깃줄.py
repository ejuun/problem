def bi(val, num):
    left = 0
    right = len(val)-1
    while left <= right:
        mid = (right+left) // 2
        if val[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return left

N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
line.sort(key=lambda x: x[0])

max_val = 0
for l in line:
    big = max(l[0], l[1])
    if max_val < big:
        max_val = big

dp = [line[0][0]]#길이
val = [line[0][1]]#값

for i in range(1, N):
    if val[-1] < line[i][1]:
        dp.append(line[i][0])
        val.append(line[i][1])
    else:
        new_val = bi(val, line[i][1])
        val[new_val] = line[i][1]
        dp[new_val] = line[i][0]

print(N - len(dp))        