N, M = map(int, input().split())

num = [0] * (M+1)
num[1] = 1

for i in range(2, M+1):
    if not num[i]:
        for j in range(2*i, M+1, i):
            num[j] = 1

for i in range(N, len(num)):
    if not num[i]:
        print(i)