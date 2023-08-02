n, m = map(int, input().split())
q = ['-'] + list(input())
a = ['='] + list(input())

dp = [[0 for _ in range(len(a))] for _ in range(len(q))]

for i in range(len(q)):
    dp[i][0] = i
for j in range(len(a)):
    dp[0][j] = j

for i in range(1, len(q)):
    for j in range(1, len(a)):
        if q[i] == a[j] or (q[i] == 'v' and a[j] == 'w') or(q[i] == 'i' and a[j] == 'j') or (q[i] == 'i' and a[j] == 'l'):
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(dp[n][m])