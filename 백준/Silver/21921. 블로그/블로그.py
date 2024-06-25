import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
hap = [0 for _ in range(N)]

hap[0] = arr[0]
for i in range(1, N):
    hap[i] = hap[i-1] + arr[i]
new_hap = [0] + hap

max_visit = 0
cnt = 0

for i in range(K-1, N+1):
    if new_hap[i] - new_hap[i-K] > max_visit:
        max_visit = new_hap[i] - new_hap[i-K]
        cnt = 1
    elif new_hap[i] - new_hap[i-K] == max_visit:
        cnt += 1
if not max_visit:
    print('SAD')
else:
    print(max_visit)
    print(cnt)