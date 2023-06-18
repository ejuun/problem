N, K = map(int, input().split())
study = [list(map(int, input().split())) for _ in range(K)]
max_time = [0] * (N+1)

for need, time in study:
    for i in range(N, time-1, -1):
        max_time[i] = max(max_time[i], max_time[i-time]+need)
print(max_time[N])