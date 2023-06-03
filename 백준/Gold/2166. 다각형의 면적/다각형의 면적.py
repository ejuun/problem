N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr += [arr[0]]
area = 0

for i in range(N):
    area += arr[i][0] * arr[i + 1][1]
    area -= arr[i][1] * arr[i + 1][0]
    
area = abs(area) / 2

print(round(area, 2))
