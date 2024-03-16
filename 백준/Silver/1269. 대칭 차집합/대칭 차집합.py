import sys
input = sys.stdin.readline

A_num, B_num = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

union = A.union(B)
inter = A.intersection(B)

print(len(union) - len(inter))