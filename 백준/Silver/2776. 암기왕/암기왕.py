import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    set1 = set(list(map(int, input().split())))
    M = int(input())
    l1 = list(map(int, input().split()))

    for num in l1:
        if num in set1:
            print(1)
        else:
            print(0)