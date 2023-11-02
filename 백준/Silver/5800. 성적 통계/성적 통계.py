import sys
input = sys.stdin.readline

K = int(input())
for i in range(1, K + 1):
    N, *lst = map(int, input().split())
    lst.sort()
    diff = 0
    for j in range(N - 1):
        if abs(lst[j + 1] - lst[j]) > diff:
            diff = abs(lst[j + 1] - lst[j])
    print('Class', i)
    print('Max', lst[-1], end=", ")
    print('Min', lst[0], end=", ")
    print('Largest gap', diff)