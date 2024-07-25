record = [0]
N, M = map(int, input().split())
score = list(map(int, input().split()))

sum = 0
num = 100001

for i in range(M):
    tep = list(input().split())
    cnt = 0
    for j in range(1, N+1):
        if tep[j] =='O':
            cnt += int(score[j-1])

    if sum < cnt:
        sum = cnt
        num = int(tep[0])
    elif sum == cnt:
        num = min(num, int(tep[0]))

print(num, sum)