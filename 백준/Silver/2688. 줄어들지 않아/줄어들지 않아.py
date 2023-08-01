dp = [0] * 65
lst = [[0 for _ in range(10)] for _ in range(65)]
dp[1] = 10
dp[2] = 55
for i in range(10):
    lst[2][i] = i+1

for i in range(3, 65):
    for j in range(10):
        if j == 0:
            lst[i][j] = 1
        else:
            lst[i][j] = lst[i][j-1] + lst[i-1][j]
    dp[i] = sum(lst[i])

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])