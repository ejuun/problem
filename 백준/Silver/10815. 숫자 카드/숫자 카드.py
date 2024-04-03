import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

dic = dict()
for i in range(N):
    dic[card[i]] = 1

for i in range(M):
    if check[i] not in dic:
        print(0, end=' ')
    else:
        print(1, end=' ')